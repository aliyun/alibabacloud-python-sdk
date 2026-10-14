# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RescaleApplicationRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        rescale_level: str = None,
        rescale_type: str = None,
        resource_selector: str = None,
        timeout: int = None,
        to_app_version: str = None,
    ):
        # The application ID. You can obtain this value by calling the ListApplications operation.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The level of the scaling region. Valid values:
        # 
        # - AreaIspCode: region ISP.
        # - RegionId: edge zone.
        # - InstanceId: instance. Scale-out indicates resource hosting. Scale-in indicates resource release.
        # 
        # Default value: AreaIspCode.
        self.rescale_level = rescale_level
        # The scaling action for resources. Valid values:
        # - Add: Provisions new resources.
        # - Del: Releases resources.
        # 
        # This parameter is required.
        self.rescale_type = rescale_type
        # The scaling resource requirements. The value is a string in JSON array format.
        # 
        # This parameter is required.
        self.resource_selector = resource_selector
        # The timeout period for asynchronous scaling, in seconds. Default value: 300.
        self.timeout = timeout
        # The application deployment version for new resources. This parameter takes effect only when resources are added. Default value: the stable version number of the application.
        self.to_app_version = to_app_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.rescale_level is not None:
            result['RescaleLevel'] = self.rescale_level

        if self.rescale_type is not None:
            result['RescaleType'] = self.rescale_type

        if self.resource_selector is not None:
            result['ResourceSelector'] = self.resource_selector

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.to_app_version is not None:
            result['ToAppVersion'] = self.to_app_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('RescaleLevel') is not None:
            self.rescale_level = m.get('RescaleLevel')

        if m.get('RescaleType') is not None:
            self.rescale_type = m.get('RescaleType')

        if m.get('ResourceSelector') is not None:
            self.resource_selector = m.get('ResourceSelector')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('ToAppVersion') is not None:
            self.to_app_version = m.get('ToAppVersion')

        return self

