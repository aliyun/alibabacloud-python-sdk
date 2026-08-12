# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAIAgentEventRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        asset_name: str = None,
        asset_type: str = None,
        current_page: int = None,
        infra_instance_id: str = None,
        infra_name: str = None,
        infra_region_id: str = None,
        lang: str = None,
        page_size: int = None,
        risk_level: str = None,
        risk_name: str = None,
        source: str = None,
        status: str = None,
        status_list: List[str] = None,
        vendor: str = None,
    ):
        # The ID of the agent application.
        self.app_id = app_id
        # Filters the agent list by application name.
        self.app_name = app_name
        # The asset name.
        self.asset_name = asset_name
        # The type of the agent asset. Valid values:
        # 1. rag
        # 2. internet
        # 3. datasets
        # 4. tool
        # 5. model
        # 6. skill
        # 7. app
        # 8. identity
        self.asset_type = asset_type
        # The current page number.
        self.current_page = current_page
        # The infrastructure instance ID.
        self.infra_instance_id = infra_instance_id
        # The infrastructure name.
        self.infra_name = infra_name
        # The infrastructure region.
        self.infra_region_id = infra_region_id
        # The language of the response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The number of entries per page.
        self.page_size = page_size
        # The risk level of the check item to query. Valid values:
        # 
        # - **high**: High.
        # - **medium**: Medium.
        # - **low**: Low.
        self.risk_level = risk_level
        # The risk name. Fuzzy match is supported.
        self.risk_name = risk_name
        # The event source. Valid values:
        # 1. cspm
        # 2. aiguard
        # 3. SASE
        # 4. SAS 
        # 5. Agent-Runtime-Guard
        self.source = source
        # The event status. Valid values:
        # 1. unhandled: Pending.
        # 2. handling: Being processed.
        # 3. fixed: Fixed.
        # 4. ignored: Ignored.
        # 5. rescanned: Rescanned.
        self.status = status
        # The list of statuses.
        self.status_list = status_list
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

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.infra_instance_id is not None:
            result['InfraInstanceId'] = self.infra_instance_id

        if self.infra_name is not None:
            result['InfraName'] = self.infra_name

        if self.infra_region_id is not None:
            result['InfraRegionId'] = self.infra_region_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.risk_name is not None:
            result['RiskName'] = self.risk_name

        if self.source is not None:
            result['Source'] = self.source

        if self.status is not None:
            result['Status'] = self.status

        if self.status_list is not None:
            result['StatusList'] = self.status_list

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

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InfraInstanceId') is not None:
            self.infra_instance_id = m.get('InfraInstanceId')

        if m.get('InfraName') is not None:
            self.infra_name = m.get('InfraName')

        if m.get('InfraRegionId') is not None:
            self.infra_region_id = m.get('InfraRegionId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('RiskName') is not None:
            self.risk_name = m.get('RiskName')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

