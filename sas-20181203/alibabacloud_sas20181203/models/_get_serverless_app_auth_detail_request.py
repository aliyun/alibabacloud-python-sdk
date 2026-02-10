# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetServerlessAppAuthDetailRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_region_id: str = None,
        machine_type: str = None,
        vendor_type: str = None,
    ):
        # SAE application ID.
        # 
        # > Obtain through the [ListMachineApps](~~ListMachineApps~~) interface.
        self.app_id = app_id
        # Application region ID.
        self.app_region_id = app_region_id
        # Server type: 
        # - **RunD**
        # - **ECI**
        self.machine_type = machine_type
        # Cloud product: 
        # - **ASK**
        # - **SAE**
        # - **ACS**
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_region_id is not None:
            result['AppRegionId'] = self.app_region_id

        if self.machine_type is not None:
            result['MachineType'] = self.machine_type

        if self.vendor_type is not None:
            result['VendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppRegionId') is not None:
            self.app_region_id = m.get('AppRegionId')

        if m.get('MachineType') is not None:
            self.machine_type = m.get('MachineType')

        if m.get('VendorType') is not None:
            self.vendor_type = m.get('VendorType')

        return self

