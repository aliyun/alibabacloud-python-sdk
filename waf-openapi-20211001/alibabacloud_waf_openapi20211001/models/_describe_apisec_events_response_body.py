# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeApisecEventsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeApisecEventsResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The security events.
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
                temp_model = main_models.DescribeApisecEventsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApisecEventsResponseBodyData(DaraModel):
    def __init__(
        self,
        all_cnt: int = None,
        api_format: str = None,
        api_id: str = None,
        api_tag: str = None,
        attack_client: str = None,
        attack_cnt_info: str = None,
        attack_ip: str = None,
        attack_ip_info: str = None,
        attack_ips: List[str] = None,
        attacker_list: List[str] = None,
        end_ts: int = None,
        event_id: str = None,
        event_info: str = None,
        event_level: str = None,
        event_tag: str = None,
        follow: int = None,
        matched_host: str = None,
        note: str = None,
        origin: str = None,
        remote_country: str = None,
        remote_region: str = None,
        request_data: str = None,
        response_data: str = None,
        start_ts: int = None,
        user_status: str = None,
    ):
        # The number of attacks.
        # >Notice: The parameter has been deprecated, please use the Attackips parameter.
        self.all_cnt = all_cnt
        # The API.
        self.api_format = api_format
        # The ID of the API that is associated with the security event.
        self.api_id = api_id
        # The business purpose of the API.
        # 
        # >  You can call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to query the business purposes of APIs.
        self.api_tag = api_tag
        # The client that is attacked.
        self.attack_client = attack_client
        # The information about the number of attacks. The value of this parameter is a JSON string that contains multiple parameters. Key indicates the timestamp in seconds, and Value indicates the number of attacks.
        self.attack_cnt_info = attack_cnt_info
        # The source IP address of the attack.
        self.attack_ip = attack_ip
        # The information about the attack source IP address. The value of this parameter is a JSON string that contains multiple parameters. The value includes the following parameters:
        # 
        # *   **ip**: the IP address
        # *   **country_id**: the country ID
        # *   **region_id**: the region ID
        # *   **cnt**: the number of attacks
        self.attack_ip_info = attack_ip_info
        # The source IP addresses of the attacks.
        self.attack_ips = attack_ips
        self.attacker_list = attacker_list
        # The end of the time range to query. This value is a UNIX timestamp in UTC. Unit: seconds.
        self.end_ts = end_ts
        # The ID of the event.
        self.event_id = event_id
        # The details of the event. The value of this parameter is a JSON string that contains multiple parameters. The value includes the following parameters:
        # 
        # *   **ip_info**: the information about the attack source IP address. This parameter corresponds to the **AttackIpInfo** response parameter.
        # *   **rule_id**: the ID of the rule corresponding to the event.
        # *   **rule_tag**: the information about the rule corresponding to the event.
        self.event_info = event_info
        # The severity level of the event. Valid values:
        # 
        # *   **high**
        # *   **medium**
        # *   **low**
        self.event_level = event_level
        # The type of the event.
        # 
        # >  You can call the [DescribeApisecRules](https://help.aliyun.com/document_detail/2859155.html) operation to query the supported event types.
        self.event_tag = event_tag
        # Indicates whether the API is followed. Valid values:
        # 
        # *   **1**: The API is followed.
        # *   **0**: The API is not followed.
        self.follow = follow
        # The domain name or IP address of the API.
        self.matched_host = matched_host
        # The remarks.
        self.note = note
        # The source of the event type. Valid values:
        # 
        # *   **custom**
        # *   **default**
        self.origin = origin
        # The country to which the attack source IP address belongs.
        self.remote_country = remote_country
        # The region to which the attack source IP address belongs.
        self.remote_region = remote_region
        # The sample API request. The value of this parameter is a JSON string that contains multiple parameters.
        self.request_data = request_data
        # The sample API response. The value of this parameter is a JSON string that contains multiple parameters.
        self.response_data = response_data
        # The beginning of the time range to query. This value is a UNIX timestamp in UTC. Unit: seconds.
        self.start_ts = start_ts
        # The event status. Valid values:
        # 
        # *   **toBeConfirmed**
        # *   **confirmed**
        # *   **ignored**
        self.user_status = user_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_cnt is not None:
            result['AllCnt'] = self.all_cnt

        if self.api_format is not None:
            result['ApiFormat'] = self.api_format

        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_tag is not None:
            result['ApiTag'] = self.api_tag

        if self.attack_client is not None:
            result['AttackClient'] = self.attack_client

        if self.attack_cnt_info is not None:
            result['AttackCntInfo'] = self.attack_cnt_info

        if self.attack_ip is not None:
            result['AttackIp'] = self.attack_ip

        if self.attack_ip_info is not None:
            result['AttackIpInfo'] = self.attack_ip_info

        if self.attack_ips is not None:
            result['AttackIps'] = self.attack_ips

        if self.attacker_list is not None:
            result['AttackerList'] = self.attacker_list

        if self.end_ts is not None:
            result['EndTs'] = self.end_ts

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_info is not None:
            result['EventInfo'] = self.event_info

        if self.event_level is not None:
            result['EventLevel'] = self.event_level

        if self.event_tag is not None:
            result['EventTag'] = self.event_tag

        if self.follow is not None:
            result['Follow'] = self.follow

        if self.matched_host is not None:
            result['MatchedHost'] = self.matched_host

        if self.note is not None:
            result['Note'] = self.note

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.remote_country is not None:
            result['RemoteCountry'] = self.remote_country

        if self.remote_region is not None:
            result['RemoteRegion'] = self.remote_region

        if self.request_data is not None:
            result['RequestData'] = self.request_data

        if self.response_data is not None:
            result['ResponseData'] = self.response_data

        if self.start_ts is not None:
            result['StartTs'] = self.start_ts

        if self.user_status is not None:
            result['UserStatus'] = self.user_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllCnt') is not None:
            self.all_cnt = m.get('AllCnt')

        if m.get('ApiFormat') is not None:
            self.api_format = m.get('ApiFormat')

        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiTag') is not None:
            self.api_tag = m.get('ApiTag')

        if m.get('AttackClient') is not None:
            self.attack_client = m.get('AttackClient')

        if m.get('AttackCntInfo') is not None:
            self.attack_cnt_info = m.get('AttackCntInfo')

        if m.get('AttackIp') is not None:
            self.attack_ip = m.get('AttackIp')

        if m.get('AttackIpInfo') is not None:
            self.attack_ip_info = m.get('AttackIpInfo')

        if m.get('AttackIps') is not None:
            self.attack_ips = m.get('AttackIps')

        if m.get('AttackerList') is not None:
            self.attacker_list = m.get('AttackerList')

        if m.get('EndTs') is not None:
            self.end_ts = m.get('EndTs')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventInfo') is not None:
            self.event_info = m.get('EventInfo')

        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')

        if m.get('EventTag') is not None:
            self.event_tag = m.get('EventTag')

        if m.get('Follow') is not None:
            self.follow = m.get('Follow')

        if m.get('MatchedHost') is not None:
            self.matched_host = m.get('MatchedHost')

        if m.get('Note') is not None:
            self.note = m.get('Note')

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('RemoteCountry') is not None:
            self.remote_country = m.get('RemoteCountry')

        if m.get('RemoteRegion') is not None:
            self.remote_region = m.get('RemoteRegion')

        if m.get('RequestData') is not None:
            self.request_data = m.get('RequestData')

        if m.get('ResponseData') is not None:
            self.response_data = m.get('ResponseData')

        if m.get('StartTs') is not None:
            self.start_ts = m.get('StartTs')

        if m.get('UserStatus') is not None:
            self.user_status = m.get('UserStatus')

        return self

