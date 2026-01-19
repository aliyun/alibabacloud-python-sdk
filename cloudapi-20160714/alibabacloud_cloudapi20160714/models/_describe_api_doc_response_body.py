# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeApiDocResponseBody(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        auth_type: str = None,
        deployed_time: str = None,
        description: str = None,
        disable_internet: bool = None,
        error_code_samples: main_models.DescribeApiDocResponseBodyErrorCodeSamples = None,
        fail_result_sample: str = None,
        force_nonce_check: bool = None,
        group_id: str = None,
        group_name: str = None,
        region_id: str = None,
        request_config: main_models.DescribeApiDocResponseBodyRequestConfig = None,
        request_id: str = None,
        request_parameters: main_models.DescribeApiDocResponseBodyRequestParameters = None,
        result_sample: str = None,
        result_type: str = None,
        stage_name: str = None,
        visibility: str = None,
    ):
        # The ID of the API.
        self.api_id = api_id
        # The name of the API
        self.api_name = api_name
        # The security authentication method. Valid values: APP, ANONYMOUS, and APPOPENID, indicating respectively Alibaba Cloud application authentication, anonymous authentication, and third-party OpenID Connect account authentication.
        self.auth_type = auth_type
        # The publishing time.
        self.deployed_time = deployed_time
        # The API description.
        self.description = description
        # *   Specifies whether to set **DisableInternet** to **true** to limit API calls to within the VPC.
        # *   If you set **DisableInternet** to **false**, the limit is lifted. The default value is false when you create an API.
        self.disable_internet = disable_internet
        # The sample error codes returned by the backend service.
        self.error_code_samples = error_code_samples
        # The sample error response from the backend service.
        self.fail_result_sample = fail_result_sample
        # *   Specifies whether to set **ForceNonceCheck** to **true** to force the check of X-Ca-Nonce during the request. This is the unique identifier of the request and is generally identified by UUID. After receiving this parameter, API Gateway verifies the validity of this parameter. The same value can be used only once within 15 minutes. This helps prevent replay attacks.
        # *   If you set **ForceNonceCheck** to **false**, the check is not performed. The default value is false when you create an API.
        self.force_nonce_check = force_nonce_check
        # The ID of the API group.
        self.group_id = group_id
        # The name of the API group.
        self.group_name = group_name
        # The region ID of the API group.
        self.region_id = region_id
        # The returned API frontend definition. It is an array consisting of RequestConfig data.
        self.request_config = request_config
        # The ID of the request.
        self.request_id = request_id
        # The returned frontend input parameters in the API. It is an array consisting of RequestParameter data.
        self.request_parameters = request_parameters
        # The sample response.
        self.result_sample = result_sample
        # The return value type.
        self.result_type = result_type
        # The name of the runtime environment. Valid values:
        # 
        # *   **RELEASE**
        # *   **TEST**
        self.stage_name = stage_name
        # Indicates whether the API is public. Valid values: PUBLIC and PRIVATE.
        self.visibility = visibility

    def validate(self):
        if self.error_code_samples:
            self.error_code_samples.validate()
        if self.request_config:
            self.request_config.validate()
        if self.request_parameters:
            self.request_parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.auth_type is not None:
            result['AuthType'] = self.auth_type

        if self.deployed_time is not None:
            result['DeployedTime'] = self.deployed_time

        if self.description is not None:
            result['Description'] = self.description

        if self.disable_internet is not None:
            result['DisableInternet'] = self.disable_internet

        if self.error_code_samples is not None:
            result['ErrorCodeSamples'] = self.error_code_samples.to_map()

        if self.fail_result_sample is not None:
            result['FailResultSample'] = self.fail_result_sample

        if self.force_nonce_check is not None:
            result['ForceNonceCheck'] = self.force_nonce_check

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_config is not None:
            result['RequestConfig'] = self.request_config.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_parameters is not None:
            result['RequestParameters'] = self.request_parameters.to_map()

        if self.result_sample is not None:
            result['ResultSample'] = self.result_sample

        if self.result_type is not None:
            result['ResultType'] = self.result_type

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('AuthType') is not None:
            self.auth_type = m.get('AuthType')

        if m.get('DeployedTime') is not None:
            self.deployed_time = m.get('DeployedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisableInternet') is not None:
            self.disable_internet = m.get('DisableInternet')

        if m.get('ErrorCodeSamples') is not None:
            temp_model = main_models.DescribeApiDocResponseBodyErrorCodeSamples()
            self.error_code_samples = temp_model.from_map(m.get('ErrorCodeSamples'))

        if m.get('FailResultSample') is not None:
            self.fail_result_sample = m.get('FailResultSample')

        if m.get('ForceNonceCheck') is not None:
            self.force_nonce_check = m.get('ForceNonceCheck')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestConfig') is not None:
            temp_model = main_models.DescribeApiDocResponseBodyRequestConfig()
            self.request_config = temp_model.from_map(m.get('RequestConfig'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestParameters') is not None:
            temp_model = main_models.DescribeApiDocResponseBodyRequestParameters()
            self.request_parameters = temp_model.from_map(m.get('RequestParameters'))

        if m.get('ResultSample') is not None:
            self.result_sample = m.get('ResultSample')

        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

class DescribeApiDocResponseBodyRequestParameters(DaraModel):
    def __init__(
        self,
        request_parameter: List[main_models.DescribeApiDocResponseBodyRequestParametersRequestParameter] = None,
    ):
        self.request_parameter = request_parameter

    def validate(self):
        if self.request_parameter:
            for v1 in self.request_parameter:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RequestParameter'] = []
        if self.request_parameter is not None:
            for k1 in self.request_parameter:
                result['RequestParameter'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.request_parameter = []
        if m.get('RequestParameter') is not None:
            for k1 in m.get('RequestParameter'):
                temp_model = main_models.DescribeApiDocResponseBodyRequestParametersRequestParameter()
                self.request_parameter.append(temp_model.from_map(k1))

        return self

class DescribeApiDocResponseBodyRequestParametersRequestParameter(DaraModel):
    def __init__(
        self,
        api_parameter_name: str = None,
        array_items_type: str = None,
        default_value: str = None,
        demo_value: str = None,
        description: str = None,
        doc_order: int = None,
        doc_show: str = None,
        enum_value: str = None,
        json_scheme: str = None,
        location: str = None,
        max_length: int = None,
        max_value: int = None,
        min_length: int = None,
        min_value: int = None,
        parameter_type: str = None,
        regular_expression: str = None,
        required: str = None,
    ):
        # The name of the parameter in the API request.
        self.api_parameter_name = api_parameter_name
        # The type of the array element.
        self.array_items_type = array_items_type
        # The default value.
        self.default_value = default_value
        # The example value.
        self.demo_value = demo_value
        # The parameter description.
        self.description = description
        # The order in which the parameter is sorted in the document.
        self.doc_order = doc_order
        # Indicates whether the document is public. Valid values: **PUBLIC** and **PRIVATE**.
        self.doc_show = doc_show
        # The hash values that are supported when **ParameterType** is set to Int, Long, Float, Double, or String. Separate values with commas (,). Examples: 1,2,3,4,9 and A,B,C,E,F.
        self.enum_value = enum_value
        # JSON scheme
        self.json_scheme = json_scheme
        # The parameter location. Valid values: BODY, HEAD, QUERY, and PATH.
        self.location = location
        # The maximum length.
        self.max_length = max_length
        # The maximum value.
        self.max_value = max_value
        # The minimum length.
        self.min_length = min_length
        # The minimum value.
        self.min_value = min_value
        # The data type of the parameter.
        self.parameter_type = parameter_type
        # The regular expression that is used for parameter validation when **ParameterType** is set to String.
        self.regular_expression = regular_expression
        # Indicates whether the parameter is required.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_parameter_name is not None:
            result['ApiParameterName'] = self.api_parameter_name

        if self.array_items_type is not None:
            result['ArrayItemsType'] = self.array_items_type

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.demo_value is not None:
            result['DemoValue'] = self.demo_value

        if self.description is not None:
            result['Description'] = self.description

        if self.doc_order is not None:
            result['DocOrder'] = self.doc_order

        if self.doc_show is not None:
            result['DocShow'] = self.doc_show

        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value

        if self.json_scheme is not None:
            result['JsonScheme'] = self.json_scheme

        if self.location is not None:
            result['Location'] = self.location

        if self.max_length is not None:
            result['MaxLength'] = self.max_length

        if self.max_value is not None:
            result['MaxValue'] = self.max_value

        if self.min_length is not None:
            result['MinLength'] = self.min_length

        if self.min_value is not None:
            result['MinValue'] = self.min_value

        if self.parameter_type is not None:
            result['ParameterType'] = self.parameter_type

        if self.regular_expression is not None:
            result['RegularExpression'] = self.regular_expression

        if self.required is not None:
            result['Required'] = self.required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiParameterName') is not None:
            self.api_parameter_name = m.get('ApiParameterName')

        if m.get('ArrayItemsType') is not None:
            self.array_items_type = m.get('ArrayItemsType')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('DemoValue') is not None:
            self.demo_value = m.get('DemoValue')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DocOrder') is not None:
            self.doc_order = m.get('DocOrder')

        if m.get('DocShow') is not None:
            self.doc_show = m.get('DocShow')

        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')

        if m.get('JsonScheme') is not None:
            self.json_scheme = m.get('JsonScheme')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')

        if m.get('MaxValue') is not None:
            self.max_value = m.get('MaxValue')

        if m.get('MinLength') is not None:
            self.min_length = m.get('MinLength')

        if m.get('MinValue') is not None:
            self.min_value = m.get('MinValue')

        if m.get('ParameterType') is not None:
            self.parameter_type = m.get('ParameterType')

        if m.get('RegularExpression') is not None:
            self.regular_expression = m.get('RegularExpression')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        return self

class DescribeApiDocResponseBodyRequestConfig(DaraModel):
    def __init__(
        self,
        body_format: str = None,
        escape_path_param: bool = None,
        post_body_description: str = None,
        request_http_method: str = None,
        request_mode: str = None,
        request_path: str = None,
        request_protocol: str = None,
    ):
        # This parameter takes effect only when the RequestMode parameter is set to MAPPING.********
        # 
        # The server data transmission method used for POST and PUT requests. Valid values: FORM and STREAM. FORM indicates that data in key-value pairs is transmitted as forms. STREAM indicates that data is transmitted as byte streams.
        self.body_format = body_format
        # Whether to escape the Path parameter, if true, the [param] on the Path will be treated as a regular character.
        self.escape_path_param = escape_path_param
        # The description of the request body.
        self.post_body_description = post_body_description
        # The HTTP method used to make the request. Valid values: GET, POST, DELETE, PUT, HEADER, TRACE, PATCH, CONNECT, and OPTIONS.
        self.request_http_method = request_http_method
        # The request mode. Valid values:
        # 
        # *   MAPPING: Parameters are mapped. Unknown parameters are filtered out.
        # *   PASSTHROUGH: Parameters are passed through.
        # *   MAPPING_PASSTHROUGH: Parameters are mapped. Unknown parameters are passed through.
        self.request_mode = request_mode
        # The API request path. If the complete API URL is `http://api.a.com:8080/object/add?key1=value1&key2=value2`, the API request path is ` /object/add  `.
        self.request_path = request_path
        # The protocol type supported by the API. Valid values: HTTP and HTTPS. Separate multiple values with commas (,), such as "HTTP,HTTPS".
        self.request_protocol = request_protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body_format is not None:
            result['BodyFormat'] = self.body_format

        if self.escape_path_param is not None:
            result['EscapePathParam'] = self.escape_path_param

        if self.post_body_description is not None:
            result['PostBodyDescription'] = self.post_body_description

        if self.request_http_method is not None:
            result['RequestHttpMethod'] = self.request_http_method

        if self.request_mode is not None:
            result['RequestMode'] = self.request_mode

        if self.request_path is not None:
            result['RequestPath'] = self.request_path

        if self.request_protocol is not None:
            result['RequestProtocol'] = self.request_protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BodyFormat') is not None:
            self.body_format = m.get('BodyFormat')

        if m.get('EscapePathParam') is not None:
            self.escape_path_param = m.get('EscapePathParam')

        if m.get('PostBodyDescription') is not None:
            self.post_body_description = m.get('PostBodyDescription')

        if m.get('RequestHttpMethod') is not None:
            self.request_http_method = m.get('RequestHttpMethod')

        if m.get('RequestMode') is not None:
            self.request_mode = m.get('RequestMode')

        if m.get('RequestPath') is not None:
            self.request_path = m.get('RequestPath')

        if m.get('RequestProtocol') is not None:
            self.request_protocol = m.get('RequestProtocol')

        return self

class DescribeApiDocResponseBodyErrorCodeSamples(DaraModel):
    def __init__(
        self,
        error_code_sample: List[main_models.DescribeApiDocResponseBodyErrorCodeSamplesErrorCodeSample] = None,
    ):
        self.error_code_sample = error_code_sample

    def validate(self):
        if self.error_code_sample:
            for v1 in self.error_code_sample:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ErrorCodeSample'] = []
        if self.error_code_sample is not None:
            for k1 in self.error_code_sample:
                result['ErrorCodeSample'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.error_code_sample = []
        if m.get('ErrorCodeSample') is not None:
            for k1 in m.get('ErrorCodeSample'):
                temp_model = main_models.DescribeApiDocResponseBodyErrorCodeSamplesErrorCodeSample()
                self.error_code_sample.append(temp_model.from_map(k1))

        return self

class DescribeApiDocResponseBodyErrorCodeSamplesErrorCodeSample(DaraModel):
    def __init__(
        self,
        code: str = None,
        description: str = None,
        message: str = None,
    ):
        # The returned error code.
        self.code = code
        # The error description.
        self.description = description
        # The returned error message.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.description is not None:
            result['Description'] = self.description

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

