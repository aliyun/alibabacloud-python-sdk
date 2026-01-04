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
        # The ID of the application. You can query the application ID by calling the ListApplications operation.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The level of resource scaling. The value is of the enumeration type. Valid values:
        # 
        # *   AreaIspCode (default): scales resources based on the Internet service provider (ISP).
        # *   RegionId: scales resources based on the edge node.
        # *   InstanceId: scales resources based on the instance ID. Resource scale-out specifies resource hosting and scale-in specifies resource release.
        # 
        # Default value: AreaIspCode.
        self.rescale_level = rescale_level
        # The scaling operation. The value must be of the enumerated data type. Valid values:
        # 
        # *   Add: adds new resources.
        # *   Del: releases resources.
        # 
        # This parameter is required.
        self.rescale_type = rescale_type
        # The required resources. The value must be a JSON string.
        # 
        # This parameter is required.
        self.resource_selector = resource_selector
        # The timeout period for asynchronous scaling. Unit: seconds. Default value: 300.
        self.timeout = timeout
        # The version number of the application deployment package. By default, the stable version number is used. This parameter takes effect only when you perform resource scale-out.
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

