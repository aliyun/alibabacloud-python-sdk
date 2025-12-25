# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeApisecApiResourcesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeApisecApiResourcesResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The API assets.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeApisecApiResourcesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApisecApiResourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        abnormal_num: int = None,
        account_event_num: int = None,
        all_cnt: int = None,
        api_format: str = None,
        api_id: str = None,
        api_info: str = None,
        api_method: str = None,
        api_sensitive: str = None,
        api_sensitive_request: str = None,
        api_sensitive_response: str = None,
        api_status: str = None,
        api_tag: str = None,
        api_type: str = None,
        auth_flag: str = None,
        bot_cnt: int = None,
        cross_border_cnt: int = None,
        event_num: int = None,
        examples: List[str] = None,
        farthest_ts: int = None,
        follow: int = None,
        lastest_ts: int = None,
        matched_host: str = None,
        note: str = None,
        resources: List[str] = None,
    ):
        # The number of API-related risks.
        self.abnormal_num = abnormal_num
        self.account_event_num = account_event_num
        # The total number of calls to this API in the previous 30 days.
        self.all_cnt = all_cnt
        # The API.
        self.api_format = api_format
        # The ID of the API.
        self.api_id = api_id
        # The API-related information. The value of this parameter is a JSON string that contains multiple parameters. The value includes the following parameters:
        # 
        # * **param_num**: the number of API parameters
        # * **request_method**: the request method
        # * **protocol**: the request protocol
        # * **api_url**: the request URL
        # * **poc_payload**: the request
        # * **request**: the sample request
        # * **response**: the sample response
        # * **param**: the request parameters
        self.api_info = api_info
        # The request method of the API. Valid values:
        # 
        # * **GET**
        # * **POST**
        # * **HEAD**
        # * **PUT**
        # * **DELETE**
        # * **CONNECT**
        # * **PATCH**
        # * **OPTIONS**
        self.api_method = api_method
        # The API-related sensitive information. The value of this parameter is a JSON string that contains multiple parameters. The value includes the following parameters:
        # 
        # * **request_sensitive_list**: the sensitive data type in the request
        # * **response_sensitive_list**: the sensitive data type in the response
        # * **sensitive_list**: sensitive data types
        # * **sensitive_level**: sensitivity level
        self.api_sensitive = api_sensitive
        # The sensitive data type in the request.
        self.api_sensitive_request = api_sensitive_request
        # The sensitive data type in the response.
        self.api_sensitive_response = api_sensitive_response
        # The API status. Valid values:
        # 
        # *   **NewbornInterface**: The API is newly added.
        # *   **OfflineInterface**: The API is inactive.
        # *   **normal**: The API is normal.
        self.api_status = api_status
        # The business purpose of the API.
        # 
        # >  You can call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to query the business purposes of APIs.
        self.api_tag = api_tag
        # The service object. Valid values:
        # 
        # *   **PublicAPI**: public services
        # *   **ThirdpartAPI**: cooperation with third-party partners
        # *   **InternalAPI**: internal office
        self.api_type = api_type
        # Indicates whether authentication is required. Valid values:
        # 
        # * **0**: Authentication is required.
        # * **1**: Authentication is not required.
        self.auth_flag = auth_flag
        # The number of bot-initiated requests in the previous 30 days.
        self.bot_cnt = bot_cnt
        # The number of the cross-border requests in the previous 30 days.
        self.cross_border_cnt = cross_border_cnt
        # The number of API-related security events.
        self.event_num = event_num
        # The sample APIs.
        self.examples = examples
        # The time when the API asset was first detected. This value is a UNIX timestamp in UTC. Unit: seconds.
        self.farthest_ts = farthest_ts
        # Specifies whether to follow the API. Valid values:
        # 
        # *   **1**: follows the API.
        # *   **0**: does not follow the API.
        self.follow = follow
        # The time at which the API was last accessed. The value is a UNIX timestamp displayed in UTC. Unit: seconds.
        self.lastest_ts = lastest_ts
        # The domain name or IP address of the API.
        self.matched_host = matched_host
        # The remarks.
        self.note = note
        # The list of protection objects corresponding to this asset.
        self.resources = resources

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormal_num is not None:
            result['AbnormalNum'] = self.abnormal_num

        if self.account_event_num is not None:
            result['AccountEventNum'] = self.account_event_num

        if self.all_cnt is not None:
            result['AllCnt'] = self.all_cnt

        if self.api_format is not None:
            result['ApiFormat'] = self.api_format

        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_info is not None:
            result['ApiInfo'] = self.api_info

        if self.api_method is not None:
            result['ApiMethod'] = self.api_method

        if self.api_sensitive is not None:
            result['ApiSensitive'] = self.api_sensitive

        if self.api_sensitive_request is not None:
            result['ApiSensitiveRequest'] = self.api_sensitive_request

        if self.api_sensitive_response is not None:
            result['ApiSensitiveResponse'] = self.api_sensitive_response

        if self.api_status is not None:
            result['ApiStatus'] = self.api_status

        if self.api_tag is not None:
            result['ApiTag'] = self.api_tag

        if self.api_type is not None:
            result['ApiType'] = self.api_type

        if self.auth_flag is not None:
            result['AuthFlag'] = self.auth_flag

        if self.bot_cnt is not None:
            result['BotCnt'] = self.bot_cnt

        if self.cross_border_cnt is not None:
            result['CrossBorderCnt'] = self.cross_border_cnt

        if self.event_num is not None:
            result['EventNum'] = self.event_num

        if self.examples is not None:
            result['Examples'] = self.examples

        if self.farthest_ts is not None:
            result['FarthestTs'] = self.farthest_ts

        if self.follow is not None:
            result['Follow'] = self.follow

        if self.lastest_ts is not None:
            result['LastestTs'] = self.lastest_ts

        if self.matched_host is not None:
            result['MatchedHost'] = self.matched_host

        if self.note is not None:
            result['Note'] = self.note

        if self.resources is not None:
            result['Resources'] = self.resources

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalNum') is not None:
            self.abnormal_num = m.get('AbnormalNum')

        if m.get('AccountEventNum') is not None:
            self.account_event_num = m.get('AccountEventNum')

        if m.get('AllCnt') is not None:
            self.all_cnt = m.get('AllCnt')

        if m.get('ApiFormat') is not None:
            self.api_format = m.get('ApiFormat')

        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiInfo') is not None:
            self.api_info = m.get('ApiInfo')

        if m.get('ApiMethod') is not None:
            self.api_method = m.get('ApiMethod')

        if m.get('ApiSensitive') is not None:
            self.api_sensitive = m.get('ApiSensitive')

        if m.get('ApiSensitiveRequest') is not None:
            self.api_sensitive_request = m.get('ApiSensitiveRequest')

        if m.get('ApiSensitiveResponse') is not None:
            self.api_sensitive_response = m.get('ApiSensitiveResponse')

        if m.get('ApiStatus') is not None:
            self.api_status = m.get('ApiStatus')

        if m.get('ApiTag') is not None:
            self.api_tag = m.get('ApiTag')

        if m.get('ApiType') is not None:
            self.api_type = m.get('ApiType')

        if m.get('AuthFlag') is not None:
            self.auth_flag = m.get('AuthFlag')

        if m.get('BotCnt') is not None:
            self.bot_cnt = m.get('BotCnt')

        if m.get('CrossBorderCnt') is not None:
            self.cross_border_cnt = m.get('CrossBorderCnt')

        if m.get('EventNum') is not None:
            self.event_num = m.get('EventNum')

        if m.get('Examples') is not None:
            self.examples = m.get('Examples')

        if m.get('FarthestTs') is not None:
            self.farthest_ts = m.get('FarthestTs')

        if m.get('Follow') is not None:
            self.follow = m.get('Follow')

        if m.get('LastestTs') is not None:
            self.lastest_ts = m.get('LastestTs')

        if m.get('MatchedHost') is not None:
            self.matched_host = m.get('MatchedHost')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        return self

