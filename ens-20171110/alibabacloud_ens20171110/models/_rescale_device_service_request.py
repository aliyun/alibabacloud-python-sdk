# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RescaleDeviceServiceRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        image_id: str = None,
        ip_type: int = None,
        rescale_level: str = None,
        rescale_type: str = None,
        resource_info: str = None,
        resource_selector: str = None,
        resource_spec: str = None,
        service_id: str = None,
        timeout: int = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The ID of the image.
        self.image_id = image_id
        # The type of the network. The value must be of the enumerated data type. Valid values:
        # 
        # *   **1** (default): Internet
        # *   **2**: internal network
        self.ip_type = ip_type
        # The region level of the scale-out. Set the value to RegionId. RegionId specifies that resource scale-out is performed based on the ID of the edge node.
        # 
        # This parameter is required.
        self.rescale_level = rescale_level
        # The scaling operation. Set the value to Add to add new resources.
        # 
        # This parameter is required.
        self.rescale_type = rescale_type
        # The information about the resource specification template. The value must be a JSON string.
        self.resource_info = resource_info
        # The required resources. The value must be a JSON string.
        # 
        # This parameter is required.
        self.resource_selector = resource_selector
        # The resource specification.
        self.resource_spec = resource_spec
        # The ID of the service.
        self.service_id = service_id
        # The timeout period for asynchronous scale-out. Unit: seconds. Default value: 300.
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.ip_type is not None:
            result['IpType'] = self.ip_type

        if self.rescale_level is not None:
            result['RescaleLevel'] = self.rescale_level

        if self.rescale_type is not None:
            result['RescaleType'] = self.rescale_type

        if self.resource_info is not None:
            result['ResourceInfo'] = self.resource_info

        if self.resource_selector is not None:
            result['ResourceSelector'] = self.resource_selector

        if self.resource_spec is not None:
            result['ResourceSpec'] = self.resource_spec

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('IpType') is not None:
            self.ip_type = m.get('IpType')

        if m.get('RescaleLevel') is not None:
            self.rescale_level = m.get('RescaleLevel')

        if m.get('RescaleType') is not None:
            self.rescale_type = m.get('RescaleType')

        if m.get('ResourceInfo') is not None:
            self.resource_info = m.get('ResourceInfo')

        if m.get('ResourceSelector') is not None:
            self.resource_selector = m.get('ResourceSelector')

        if m.get('ResourceSpec') is not None:
            self.resource_spec = m.get('ResourceSpec')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

