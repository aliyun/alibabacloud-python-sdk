# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeApisecAbnormalsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeApisecAbnormalsResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of security risks.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # The total number of security risks returned.
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
                temp_model = main_models.DescribeApisecAbnormalsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApisecAbnormalsResponseBodyData(DaraModel):
    def __init__(
        self,
        abnormal_event_number: int = None,
        abnormal_id: str = None,
        abnormal_info: str = None,
        abnormal_level: str = None,
        abnormal_tag: str = None,
        abnromal_status: str = None,
        api_format: str = None,
        api_id: str = None,
        api_tag: str = None,
        discover_time: int = None,
        examples: List[str] = None,
        first_time: int = None,
        follow: int = None,
        ignore_time: int = None,
        lastest_time: int = None,
        latest_discover_time: int = None,
        matched_host: str = None,
        note: str = None,
        origin: str = None,
        user_status: str = None,
    ):
        # The number of risk events that are associated with the security risk.
        self.abnormal_event_number = abnormal_event_number
        # The ID of the security risk.
        self.abnormal_id = abnormal_id
        # The details of the security risk in JSON format. The JSON object contains the following fields:
        # 
        # - **rule**: The detection rule that triggered the security risk.
        # 
        # - **data_type**: The type of sensitive data.
        # 
        # - **custom_rule_name**: The name of the custom rule.
        # 
        # - **rule_name**: The name of the built-in rule.
        self.abnormal_info = abnormal_info
        # The severity level of the security risk. Valid values:
        # 
        # - **high**: High.
        # 
        # - **medium**: Medium.
        # 
        # - **low**: Low.
        self.abnormal_level = abnormal_level
        # The type of the security risk.
        # 
        # > Call [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) to query the supported risk types.
        self.abnormal_tag = abnormal_tag
        # The processing status of the security risk.
        self.abnromal_status = abnromal_status
        # The path of the API that is associated with the security risk.
        self.api_format = api_format
        # The ID of the API that is associated with the security risk.
        self.api_id = api_id
        # The business purpose of the API.
        # 
        # > Call [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) to query the supported business purposes.
        self.api_tag = api_tag
        # The time when the security risk was first detected. The value is a UNIX timestamp. Unit: seconds.
        self.discover_time = discover_time
        # The list of security risk samples.
        self.examples = examples
        # The time when the API was first discovered. The value is a UNIX timestamp. Unit: seconds.
        self.first_time = first_time
        # Indicates whether the security risk is being followed. Valid values:
        # 
        # - **1**: The security risk is being followed.
        # 
        # - **0** (default): The security risk is not being followed.
        self.follow = follow
        # The time when the security risk was marked as ignored. The value is a UNIX timestamp. Unit: seconds.
        self.ignore_time = ignore_time
        # The most recent time when the API was accessed. The value is a UNIX timestamp. Unit: seconds.
        self.lastest_time = lastest_time
        # The most recent time when the security risk was detected. The value is a UNIX timestamp. Unit: seconds.
        self.latest_discover_time = latest_discover_time
        # The domain name or IP address that the API resides on.
        self.matched_host = matched_host
        # The remarks for the security risk.
        self.note = note
        # The source of the risk detection rule. Valid values:
        # 
        # - **custom**: Custom rule.
        # 
        # - **default**: Built-in rule.
        self.origin = origin
        # The handling status of the security risk. Valid values:
        # 
        # - **toBeConfirmed**: To be confirmed.
        # 
        # - **confirmed**: Confirmed.
        # 
        # - **toBeFixed**: To be fixed.
        # 
        # - **fixed**: Fixed (manually verified).
        # 
        # - **ignored**: Ignored.
        # 
        # - **toBeVerified**: To be verified by the system.
        # 
        # - **notFixed**: Verification failed.
        # 
        # - **systemFixed**: Fixed (verified by the system).
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abnormal_event_number is not None:
            result['AbnormalEventNumber'] = self.abnormal_event_number

        if self.abnormal_id is not None:
            result['AbnormalId'] = self.abnormal_id

        if self.abnormal_info is not None:
            result['AbnormalInfo'] = self.abnormal_info

        if self.abnormal_level is not None:
            result['AbnormalLevel'] = self.abnormal_level

        if self.abnormal_tag is not None:
            result['AbnormalTag'] = self.abnormal_tag

        if self.abnromal_status is not None:
            result['AbnromalStatus'] = self.abnromal_status

        if self.api_format is not None:
            result['ApiFormat'] = self.api_format

        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_tag is not None:
            result['ApiTag'] = self.api_tag

        if self.discover_time is not None:
            result['DiscoverTime'] = self.discover_time

        if self.examples is not None:
            result['Examples'] = self.examples

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.follow is not None:
            result['Follow'] = self.follow

        if self.ignore_time is not None:
            result['IgnoreTime'] = self.ignore_time

        if self.lastest_time is not None:
            result['LastestTime'] = self.lastest_time

        if self.latest_discover_time is not None:
            result['LatestDiscoverTime'] = self.latest_discover_time

        if self.matched_host is not None:
            result['MatchedHost'] = self.matched_host

        if self.note is not None:
            result['Note'] = self.note

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.user_status is not None:
            result['UserStatus'] = self.user_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbnormalEventNumber') is not None:
            self.abnormal_event_number = m.get('AbnormalEventNumber')

        if m.get('AbnormalId') is not None:
            self.abnormal_id = m.get('AbnormalId')

        if m.get('AbnormalInfo') is not None:
            self.abnormal_info = m.get('AbnormalInfo')

        if m.get('AbnormalLevel') is not None:
            self.abnormal_level = m.get('AbnormalLevel')

        if m.get('AbnormalTag') is not None:
            self.abnormal_tag = m.get('AbnormalTag')

        if m.get('AbnromalStatus') is not None:
            self.abnromal_status = m.get('AbnromalStatus')

        if m.get('ApiFormat') is not None:
            self.api_format = m.get('ApiFormat')

        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiTag') is not None:
            self.api_tag = m.get('ApiTag')

        if m.get('DiscoverTime') is not None:
            self.discover_time = m.get('DiscoverTime')

        if m.get('Examples') is not None:
            self.examples = m.get('Examples')

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('Follow') is not None:
            self.follow = m.get('Follow')

        if m.get('IgnoreTime') is not None:
            self.ignore_time = m.get('IgnoreTime')

        if m.get('LastestTime') is not None:
            self.lastest_time = m.get('LastestTime')

        if m.get('LatestDiscoverTime') is not None:
            self.latest_discover_time = m.get('LatestDiscoverTime')

        if m.get('MatchedHost') is not None:
            self.matched_host = m.get('MatchedHost')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')

        return self

