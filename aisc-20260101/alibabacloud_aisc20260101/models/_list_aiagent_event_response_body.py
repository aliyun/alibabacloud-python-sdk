# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aisc20260101 import models as main_models
from darabonba.model import DaraModel

class ListAIAgentEventResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListAIAgentEventResponseBodyData] = None,
        page_info: main_models.ListAIAgentEventResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The list of event information returned.
        self.data = data
        # The pagination information.
        self.page_info = page_info
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAIAgentEventResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListAIAgentEventResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAIAgentEventResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        next_token: str = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The NextToken value returned when the NextToken-based pagination method is used.
        self.next_token = next_token
        # The number of entries per page.
        self.page_size = page_size
        # The total number of records in the query result.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAIAgentEventResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        asset_name: str = None,
        asset_type: str = None,
        check_time: str = None,
        handle_time: str = None,
        id: int = None,
        infra_instance_id: str = None,
        infra_internet_ip: str = None,
        infra_intranet_ip: str = None,
        infra_name: str = None,
        infra_region_id: str = None,
        infra_type: str = None,
        risk_desc: str = None,
        risk_level: str = None,
        risk_name: str = None,
        skill_id: int = None,
        source: str = None,
        status: str = None,
        vendor: str = None,
    ):
        # The application ID.
        self.app_id = app_id
        # The application name.
        self.app_name = app_name
        # The asset name.
        self.asset_name = asset_name
        # The type of the risky asset. Valid values:
        # 1. rag
        # 2. internet
        # 3. datasets
        # 4. tool
        # 5. model
        # 6. skill
        # 7. app
        # 8. identity
        self.asset_type = asset_type
        # The check time.
        self.check_time = check_time
        # The event handling time.
        self.handle_time = handle_time
        # The primary key ID.
        self.id = id
        # The infrastructure instance ID.
        self.infra_instance_id = infra_instance_id
        # The public IP address of the infrastructure.
        self.infra_internet_ip = infra_internet_ip
        # The private IP address of the infrastructure.
        self.infra_intranet_ip = infra_intranet_ip
        # The infrastructure name.
        self.infra_name = infra_name
        # The infrastructure region.
        self.infra_region_id = infra_region_id
        # The infrastructure type.
        self.infra_type = infra_type
        # The risk description.
        self.risk_desc = risk_desc
        # The risk level of the detected alert. Valid values:
        # 
        # - **high**: High.
        # - **medium**: Medium.
        # - **low**: Low.
        self.risk_level = risk_level
        # The risk name.
        self.risk_name = risk_name
        self.skill_id = skill_id
        # The event source. Valid values:
        # 1. cspm
        # 2. aiguard
        # 3. SASE
        # 4. SAS 
        # 5. Agent-Runtime-Guard
        self.source = source
        # The status. Valid values:
        # 1. unhandled: Pending.
        # 2. handling: Being processed.
        # 3. fixed: Fixed.
        # 4. ignored: Ignored.
        # 5. rescanned: Rescanned.
        self.status = status
        # The cloud asset vendor. Valid values:
        # - **DIFY**: DIFY.
        # - **BAILIAN**: BAILIAN.
        # - **VOLCAI**: VOLCAI.
        # - **AGENTRUN**: AGENTRUN.
        # - **PAI**: PAI.
        # - **OpenClaw**: OpenClaw.
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.asset_name is not None:
            result['AssetName'] = self.asset_name

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.check_time is not None:
            result['CheckTime'] = self.check_time

        if self.handle_time is not None:
            result['HandleTime'] = self.handle_time

        if self.id is not None:
            result['Id'] = self.id

        if self.infra_instance_id is not None:
            result['InfraInstanceId'] = self.infra_instance_id

        if self.infra_internet_ip is not None:
            result['InfraInternetIp'] = self.infra_internet_ip

        if self.infra_intranet_ip is not None:
            result['InfraIntranetIp'] = self.infra_intranet_ip

        if self.infra_name is not None:
            result['InfraName'] = self.infra_name

        if self.infra_region_id is not None:
            result['InfraRegionId'] = self.infra_region_id

        if self.infra_type is not None:
            result['InfraType'] = self.infra_type

        if self.risk_desc is not None:
            result['RiskDesc'] = self.risk_desc

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.risk_name is not None:
            result['RiskName'] = self.risk_name

        if self.skill_id is not None:
            result['SkillId'] = self.skill_id

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('CheckTime') is not None:
            self.check_time = m.get('CheckTime')

        if m.get('HandleTime') is not None:
            self.handle_time = m.get('HandleTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InfraInstanceId') is not None:
            self.infra_instance_id = m.get('InfraInstanceId')

        if m.get('InfraInternetIp') is not None:
            self.infra_internet_ip = m.get('InfraInternetIp')

        if m.get('InfraIntranetIp') is not None:
            self.infra_intranet_ip = m.get('InfraIntranetIp')

        if m.get('InfraName') is not None:
            self.infra_name = m.get('InfraName')

        if m.get('InfraRegionId') is not None:
            self.infra_region_id = m.get('InfraRegionId')

        if m.get('InfraType') is not None:
            self.infra_type = m.get('InfraType')

        if m.get('RiskDesc') is not None:
            self.risk_desc = m.get('RiskDesc')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RiskName') is not None:
            self.risk_name = m.get('RiskName')

        if m.get('SkillId') is not None:
            self.skill_id = m.get('SkillId')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

