# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListZonesRequest(DaraModel):
    def __init__(
        self,
        biz_region_id: str = None,
        os_type: str = None,
        product_type: str = None,
    ):
        # The region ID. Required. Specifies the region for which you want to query available zones. All returned zones are located in this region.
        # 
        # The value must be a region ID supported by App Streaming. You can call [ListRegions](~~ListRegions~~) to query the supported region IDs. If you specify an unsupported region, the error code InvalidParameter.ValueInvalid is returned.
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        # The operating system type. Required. Specifies the operating system used by the resource. This parameter and ProductType together determine the available zones. The value is case-insensitive. Use one of the following values:
        # 
        # Valid values:
        # 
        # - Windows: Windows operating system
        # - Linux: Linux operating system
        # - Android: Android operating system
        # 
        # This parameter is required.
        self.os_type = os_type
        # The product type. Required. Specifies the product for which you want to query available zones. The list of available zones is returned based on the available resources of the product in the specified region. The value is case-insensitive. Use one of the following values:
        # 
        # Valid values:
        # 
        # - CloudApp: App Streaming
        # - CloudBrowser: Cloud Browser
        # - WuyingServer: Enterprise Edition workstation
        # - WuyingWorkstation: Personal Edition Linggou container workstation
        # - WuyingWorkstationTeam: Team Edition Linggou container workstation
        # - WuyingWorkstationBusiness: Dedicated Edition Linggou container workstation
        # - AndroidCloud: Cloud Phone
        # - AIAgent: AgentBay (AI agent)
        # 
        # This parameter is required.
        self.product_type = product_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        return self

