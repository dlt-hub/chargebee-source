from base64 import b64encode
from typing import Dict, Literal, Tuple, TypedDict, Optional

from dlt.common.configuration.specs.base_configuration import BaseConfiguration, configspec


class CredentialsHttpParams(TypedDict):
    cookies: Dict[str, str]
    params: Dict[str, str]
    headers: Dict[str, str]


@configspec
class _ApiKeyCredentialsBase(BaseConfiguration):
    type: Literal["apiKey"] = "apiKey"
    location: Literal["header", "cookie", "param"]  # Alias for scheme "in" field
    name: str
    api_key: str

    def to_http_params(self) -> CredentialsHttpParams:
        result: CredentialsHttpParams = dict(cookies={}, headers={}, params={})
        result[self.location + "s"][self.name] = self.api_key  # type: ignore
        return result

    def parse_native_representation(self, native_value: str) -> None:
        if not isinstance(native_value, str):
            raise ValueError("Api Key value must be a string")
        self.api_key = native_value


@configspec
class _HttpBasicCredentialsBase(BaseConfiguration):
    type: Literal["http"] = "http"
    scheme: Literal["basic"] = "basic"
    api_key: str
    password: Optional[str]

    def to_http_params(self) -> CredentialsHttpParams:
        cred = f"{self.api_key}:{self.password}" if self.password else f"{self.username}"
        encoded = b64encode(f"{cred}".encode()).decode()
        return dict(cookies={}, headers={"Authorization": "Basic " + encoded}, params={})

    def parse_native_representation(self, native_value: Tuple[str, str]) -> None:
        username, password = native_value
        if not isinstance(username, str) or not isinstance(password, str):
            raise ValueError("Value must be a tuple of ('username', 'password')")
        self.username, self.password = username, password


@configspec
class _HttpBasicApiKeyBase(BaseConfiguration):
    type: Literal["http"] = "http"
    scheme: Literal["basic"] = "basic"
    api_key: str

    def to_http_params(self) -> CredentialsHttpParams:
        encoded = b64encode(f"{self.api_key}".encode()).decode()
        return dict(cookies={}, headers={"Authorization": "Basic " + encoded}, params={})

    def parse_native_representation(self, native_value: Tuple[str, str]) -> None:
        api_key = native_value
        if not isinstance(api_key, str):
            raise ValueError("Value must be a str of 'api_key'")
        self.api_key= api_key


@configspec
class _HttpBearerCredentialsBase(BaseConfiguration):
    type: Literal["http"] = "http"
    scheme: Literal["bearer"] = "bearer"
    token: str

    def to_http_params(self) -> CredentialsHttpParams:
        return dict(cookies={}, headers={"Authorization": "Bearer " + self.token}, params={})

    def parse_native_representation(self, native_value: str) -> None:
        if not isinstance(native_value, str):
            raise ValueError("Http bearer value must be a string")
        self.token = native_value


@configspec
class _OAuth2CredentialsBase(BaseConfiguration):
    # TODO: Separate class for flows (implcit, authorization_code, client_credentials, etc)
    type: Literal["oauth2"] = "oauth2"
    access_token: str

    def to_http_params(self) -> CredentialsHttpParams:
        return dict(cookies={}, headers={"Authorization": "Bearer " + self.access_token}, params={})

    def parse_native_representation(self, native_value: str) -> None:
        if not isinstance(native_value, str):
            raise ValueError("OAuth2 access token value must be a string")
        self.access_token = native_value
