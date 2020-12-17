[← Usage](0-Usage-EN.md) | Client & Credentials[(中文)](1-Client-CN.md) | [Home →](../../README.md)

![Alternate text](https://aliyunsdk-pages.alicdn.com/icons/AlibabaCloud.svg)

# Client & Credentials

## Usage

Before you begin, you need to sign up for an Alibaba Cloud account and retrieve your [Credentials](https://usercenter.console.aliyun.com/#/manage/ak).

### Using AccessKey call

```python

from alibabacloud_ocr20191230.client import Client
from alibabacloud_ocr20191230.models import GetAsyncJobResultRequest
from alibabacloud_tea_rpc.models import Config
from alibabacloud_tea_util.models import RuntimeOptions

config = Config(
    access_key_id='<access_key_id>',
    access_key_secret='<access_key_secret>'
)

# create and initialize a Client instance
client = Client(config)

request = GetAsyncJobResultRequest(
    job_id='<job_id>'
)

runtime_options = RuntimeOptions()
response = client.get_async_job_result(request, runtime_options)

print(response.to_map())


```

### Credential Type

#### access_key

Setup access_key credential through [User Information Management][ak], it have full authority over the account, please keep it safe. Sometimes for security reasons, you cannot hand over a primary account AccessKey with full access to the developer of a project. You may create a sub-account [RAM Sub-account][ram] , grant its [authorization][permissions]，and use the AccessKey of RAM Sub-account.

```python
from alibabacloud_credentials.client import Client
from alibabacloud_credentials.models import Config

config = Config(
    type='access_key',                    # credential type
    access_key_id='accessKeyId',          # AccessKeyId
    access_key_secret='accessKeySecret',  # AccessKeySecret
)
cred = Client(config)

access_key_id = cred.get_access_key_id()
access_key_secret = cred.get_access_key_secret()
cred_type = cred.get_type()
```

#### sts

Create a temporary security credential by applying Temporary Security Credentials (TSC) through the Security Token Service (STS).

```python
from alibabacloud_credentials.client import Client
from alibabacloud_credentials.models import Config

config = Config(
    type='sts',                           # credential type
    access_key_id='accessKeyId',          # AccessKeyId
    access_key_secret='accessKeySecret',  # AccessKeySecret
    security_token='securityToken'        # STS Token
)
cred = Client(config)

access_key_id = cred.get_access_key_id()
access_key_secret = cred.get_access_key_secret()
security_token = cred.get_security_token()
cred_type = cred.get_type()
```

#### ram_role_arn

By specifying [RAM Role][RAM Role], the credential will be able to automatically request maintenance of STS Token. If you want to limit the permissions([How to make a policy][policy]) of STS Token, you can assign value for `Policy`.

```python
from alibabacloud_credentials.client import Client
from alibabacloud_credentials.models import Config

config = Config(
    type='ram_role_arn',                  # credential type
    access_key_id='accessKeyId',          # AccessKeyId
    access_key_secret='accessKeySecret',  # AccessKeySecret
    security_token='securityToken',       # STS Token
    role_arn='roleArn',                   # Format: acs:ram::USER_ID:role/ROLE_NAME
    role_session_name='roleSessionName',  # Role Session Name
    policy='policy',                      # Not required, limit the permissions of STS Token
    role_session_expiration=3600          # Not required, limit the Valid time of STS Token
)
cred = Client(config)

access_key_id = cred.get_access_key_id()
access_key_secret = cred.get_access_key_secret()
security_token = cred.get_security_token()
cred_type = cred.get_type()
```

#### ecs_ram_role

By specifying the role name, the credential will be able to automatically request maintenance of STS Token.

```python
from alibabacloud_credentials.client import Client
from alibabacloud_credentials.models import Config

config = Config(
    type='ecs_ram_role',      # credential type
    role_name='roleName'      # `roleName` is optional. It will be retrieved automatically if not set. It is highly recommended to set it up to reduce requests.
)
cred = Client(config)

access_key_id = cred.get_access_key_id()
access_key_secret = cred.get_access_key_secret()
security_token = cred.get_security_token()
cred_type = cred.get_type()
```

#### rsa_key_pair

By specifying the public key ID and the private key file, the credential will be able to automatically request maintenance of the AccessKey before sending the request. Only Japan station is supported.

```python
from alibabacloud_credentials.client import Client
from alibabacloud_credentials.models import Config

config = Config(
    type='rsa_key_pair',                  # credential type
    private_key_file='privateKeyFile',    # The file path to store the PrivateKey
    public_key_id='publicKeyId'           # PublicKeyId of your account
)
cred = Client(config)

access_key_id = cred.get_access_key_id()
access_key_secret = cred.get_access_key_secret()
security_token = cred.get_security_token()
cred_type = cred.get_type()
```

#### bearer

If credential is required by the Cloud Call Centre (CCC), please apply for Bearer Token maintenance by yourself.

```python
from alibabacloud_credentials.client import Client
from alibabacloud_credentials.models import Config

config = Config(
    type='bearer',                        # credential type
    bearer_token='bearerToken',           # BearerToken
)
cred = Client(config)

access_key_id = cred.get_access_key_id()
access_key_secret = cred.get_access_key_secret()
security_token = cred.get_security_token()
cred_type = cred.get_type()
```

### Use the default credential provider chain

```python
from alibabacloud_credentials.client import Client as CredClient
from alibabacloud_ocr20191230.client import Client as OcrClient
from alibabacloud_ocr20191230.models import GetAsyncJobResultRequest
from alibabacloud_tea_rpc.models import Config
from alibabacloud_tea_util.models import RuntimeOptions

cred = CredClient()
config = Config(credential=cred)

client = OcrClient(config)

request = GetAsyncJobResultRequest(
    job_id='<job_id>'
)

runtime_options = RuntimeOptions()
response = client.get_async_job_result(request, runtime_options)
```

The default credential provider chain looks for available credentials, with following order:

1.Environment Credentials

Look for environment credentials in environment variable. If the `ALIBABA_CLOUD_ACCESS_KEY_ID` and `ALIBABA_CLOUD_ACCESS_KEY_SECRET` environment variables are defined and are not empty, the program will use them to create default credentials.

2.Credentials File

If there is `~/.alibabacloud/credentials default file (Windows shows C:\Users\USER_NAME\.alibabacloud\credentials)`, the program automatically creates credentials with the specified type and name. The default file is not necessarily exist, but a parse error will throw an exception. The name of configuration item is lowercase.This configuration file can be shared between different projects and between different tools. Because it is outside of the project and will not be accidentally committed to the version control. The path to the default file can be modified by defining the `ALIBABA_CLOUD_CREDENTIALS_FILE` environment variable. If not configured, use the default configuration `default`. You can also set the environment variables `ALIBABA_CLOUD_PROFILE` to use the configuration.

```ini
[default]                          # default setting
enable = true                      # Enable，Enabled by default if this option is not present
type = access_key                  # Certification type: access_key
access_key_id = foo                # Key
access_key_secret = bar            # Secret

[client1]                          # configuration that is named as `client1`
type = ecs_ram_role                # Certification type: ecs_ram_role
role_name = EcsRamRoleTest         # Role Name

[client2]                          # configuration that is named as `client2`
enable = false                     # Disable
type = ram_role_arn                # Certification type: ram_role_arn
region_id = cn-test
policy = test                      # optional Specify permissions
access_key_id = foo
access_key_secret = bar
role_arn = role_arn
role_session_name = session_name   # optional

[client3]                          # configuration that is named as `client3`
type = rsa_key_pair                # Certification type: rsa_key_pair
public_key_id = publicKeyId        # Public Key ID
private_key_file = /your/pk.pem    # Private Key file
```

3.Instance RAM Role

If the environment variable `ALIBABA_CLOUD_ECS_METADATA` is defined and not empty, the program will take the value of the environment variable as the role name and request <http://100.100.100.200/latest/meta-data/ram/security-credentials/> to get the temporary Security credentials.
