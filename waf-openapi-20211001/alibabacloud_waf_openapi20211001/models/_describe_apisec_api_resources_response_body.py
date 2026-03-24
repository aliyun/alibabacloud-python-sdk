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
        # The list of API assets.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # The total number of returned entries.
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
        # The number of threats associated with the API.
        self.abnormal_num = abnormal_num
        # The number of account security events associated with the API.
        self.account_event_num = account_event_num
        # The total number of requests in the last 30 days.
        self.all_cnt = all_cnt
        # The API endpoint path.
        self.api_format = api_format
        # The ID of the API.
        self.api_id = api_id
        # The detailed information about the API. The value is a JSON string that contains the following fields:
        # 
        # - **param_num**: the number of API parameters.
        # 
        # - **request_method**: the request method.
        # 
        # - **protocol**: the request protocol.
        # 
        # - **api_url**: the request URL.
        # 
        # - **poc_payload**: the request.
        # 
        # - **request**: the request sample.
        # 
        # - **response**: the response sample.
        # 
        # - **param**: the request parameters.
        # 
        # > This parameter is returned only when you specify the **ApiId** request parameter.
        self.api_info = api_info
        # The HTTP request method of the API. Valid values: **GET**, **POST**, **HEAD**, **PUT**, **DELETE**, **CONNECT**, **PATCH**, and **OPTIONS**.
        self.api_method = api_method
        # The sensitive data classification of the API. The value is a JSON string that contains the following fields:
        # 
        # - **request_sensitive_list**: the list of sensitive data types in the request.
        # 
        # - **response_sensitive_list**: the list of sensitive data types in the response.
        # 
        # - **sensitive_list**: the list of sensitive data types.
        # 
        # - **sensitive_level**: the sensitivity level.
        self.api_sensitive = api_sensitive
        # The types of sensitive data detected in the API request. The value is a JSON array of sensitive data type IDs.
        self.api_sensitive_request = api_sensitive_request
        # The types of sensitive data detected in the API response. The value is a JSON array of sensitive data type IDs.
        self.api_sensitive_response = api_sensitive_response
        # The lifecycle status of the API. Valid values:
        # 
        # - **NewbornInterface**: newly discovered.
        # 
        # - **OfflineInterface**: inactive.
        # 
        # - **normal**: active.
        self.api_status = api_status
        # The business purpose of the API.
        # 
        # > Call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to obtain the supported business purposes.
        self.api_tag = api_tag
        # The type of service that the API serves. Valid values:
        # 
        # - **PublicAPI**: public-facing service.
        # 
        # - **ThirdpartAPI**: third-party service.
        # 
        # - **InternalAPI**: internal service.
        self.api_type = api_type
        # Indicates whether the API requires authentication. Valid values:
        # 
        # - **0**: The API requires authentication.
        # 
        # - **1**: The API does not require authentication.
        self.auth_flag = auth_flag
        # The number of bot requests in the last 30 days.
        self.bot_cnt = bot_cnt
        # The number of cross-border requests in the last 30 days.
        self.cross_border_cnt = cross_border_cnt
        # The number of security events associated with the API.
        self.event_num = event_num
        # The list of API samples.
        self.examples = examples
        # The time when the API was first discovered. The value is a UNIX timestamp. Unit: seconds.
        self.farthest_ts = farthest_ts
        # Indicates whether the API is followed. Valid values:
        # 
        # - **1**: The API is followed.
        # 
        # - **0**: The API is not followed.
        self.follow = follow
        # The time of the most recent access to the API. The value is a UNIX timestamp. Unit: seconds.
        self.lastest_ts = lastest_ts
        # The domain name or IP address that the API resides on.
        self.matched_host = matched_host
        # The remarks of the API asset.
        self.note = note
        # The list of protected objects associated with the API.
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

