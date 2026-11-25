# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeThreatEventDetailResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        threat_event_detail: main_models.DescribeThreatEventDetailResponseBodyThreatEventDetail = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the security event.
        self.threat_event_detail = threat_event_detail

    def validate(self):
        if self.threat_event_detail:
            self.threat_event_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.threat_event_detail is not None:
            result['ThreatEventDetail'] = self.threat_event_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ThreatEventDetail') is not None:
            temp_model = main_models.DescribeThreatEventDetailResponseBodyThreatEventDetail()
            self.threat_event_detail = temp_model.from_map(m.get('ThreatEventDetail'))

        return self

class DescribeThreatEventDetailResponseBodyThreatEventDetail(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        event_block: str = None,
        event_cnt: str = None,
        event_condition: str = None,
        event_intelligence: str = None,
        event_level: str = None,
        event_src: str = None,
        event_src_country: str = None,
        event_src_region: str = None,
        event_suggest: str = None,
        event_tag: str = None,
        is_persistent: int = None,
    ):
        # The most recent attack time. The value is a UNIX timestamp in UTC. Unit: seconds.
        self.end_time = end_time
        # The number of blocked attacks.
        self.event_block = event_block
        # The total number of attacks.
        self.event_cnt = event_cnt
        # The filter condition for the log query feature. The value is a string converted from a **JSON** structure constructed with a series of parameters.
        self.event_condition = event_condition
        # The threat intelligence associated with the event. The value is a string converted from a **JSON** array.
        self.event_intelligence = event_intelligence
        # The severity level of the event. Valid values:
        # 
        # - **critical**: critical.
        # - **high**: high.
        # - **medium**: medium.
        # - **low**: low.
        self.event_level = event_level
        # The attack source IP addresses.
        # > A security event may have multiple attack source IP addresses. This operation returns only one.
        self.event_src = event_src
        # The country to which the attack source IP addresses belong.
        self.event_src_country = event_src_country
        # The region to which the attack source IP addresses belong.
        self.event_src_region = event_src_region
        # The security suggestion. Valid values:
        # 
        # - **ProtectInterface**: The Attack Target is suspected to be a backend management address. If the address has fixed access characteristics, configure custom rules in the access control module to restrict access.
        # - **BlockArea**: Monitor the source region of the attack. If the attack source differs from the normal regional distribution of your service, configure Location Blacklist or IP blacklist rules in the access control module to restrict access.
        # - **SwitchBlock**: The current rule protection is in alerting mode. To ensure service security, switch to block mode. Before switching, check for false positives.
        # - **FixBug**: Check whether the Attack Target has a security vulnerability. If the security vulnerability exists, fix it promptly to prevent exploitation by attackers.
        # - **SwitchStrict**: If normal service is not affected, adjust the policy of modules such as rule protection and scan protection to a stricter pattern. Before adjusting the policy, check for false positives.
        # - **ProtectFile**: Check whether sensitive files or paths exist under the target domain name to prevent detection and exploitation by attackers.
        # - **BlockIP**: The source IP address of the attack is highly malicious. Monitor the IP address. If normal service is not affected, block access from the malicious IP address by using an IP blacklist.
        # - **KeepConcerned**: No risks are detected. Continue to monitor the event.
        self.event_suggest = event_suggest
        # The name of the event. Valid values:
        # 
        # - **MultipleDomainDirscan**: directory and file scanning targeting multiple domain names
        # - **SingleDomainDirscan**: directory and file scanning targeting a single domain name
        # - **MultipleDomainWebscan**: web vulnerability scanning targeting multiple domain names
        # - **SingleDomainWebscan**: web vulnerability scanning targeting a single domain name
        # - **MultipleDomainWebattack**: web vulnerability attacks targeting multiple domain names
        # - **SingleDomainWebattack**: web vulnerability attacks targeting a single domain name
        # - **SingleURLWebattack**: web vulnerability attacks targeting a specific URL
        # - **SingleURLSqlattack**: SQL injection attacks targeting a specific URL
        # - **SingleURLXssattack**: XSS attacks targeting a specific URL
        # - **WebshellUpload**: attack behavior attempting to upload backdoor trojans
        # - **RandomVulnTest**: random web vulnerability detection behavior
        self.event_tag = event_tag
        # Indicates whether the attack event is a targeted persistent attack event. Valid values:
        # 
        # - **0**: non-persistent attack.
        # 
        # - **1**: persistent attack.
        self.is_persistent = is_persistent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_block is not None:
            result['EventBlock'] = self.event_block

        if self.event_cnt is not None:
            result['EventCnt'] = self.event_cnt

        if self.event_condition is not None:
            result['EventCondition'] = self.event_condition

        if self.event_intelligence is not None:
            result['EventIntelligence'] = self.event_intelligence

        if self.event_level is not None:
            result['EventLevel'] = self.event_level

        if self.event_src is not None:
            result['EventSrc'] = self.event_src

        if self.event_src_country is not None:
            result['EventSrcCountry'] = self.event_src_country

        if self.event_src_region is not None:
            result['EventSrcRegion'] = self.event_src_region

        if self.event_suggest is not None:
            result['EventSuggest'] = self.event_suggest

        if self.event_tag is not None:
            result['EventTag'] = self.event_tag

        if self.is_persistent is not None:
            result['IsPersistent'] = self.is_persistent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventBlock') is not None:
            self.event_block = m.get('EventBlock')

        if m.get('EventCnt') is not None:
            self.event_cnt = m.get('EventCnt')

        if m.get('EventCondition') is not None:
            self.event_condition = m.get('EventCondition')

        if m.get('EventIntelligence') is not None:
            self.event_intelligence = m.get('EventIntelligence')

        if m.get('EventLevel') is not None:
            self.event_level = m.get('EventLevel')

        if m.get('EventSrc') is not None:
            self.event_src = m.get('EventSrc')

        if m.get('EventSrcCountry') is not None:
            self.event_src_country = m.get('EventSrcCountry')

        if m.get('EventSrcRegion') is not None:
            self.event_src_region = m.get('EventSrcRegion')

        if m.get('EventSuggest') is not None:
            self.event_suggest = m.get('EventSuggest')

        if m.get('EventTag') is not None:
            self.event_tag = m.get('EventTag')

        if m.get('IsPersistent') is not None:
            self.is_persistent = m.get('IsPersistent')

        return self

