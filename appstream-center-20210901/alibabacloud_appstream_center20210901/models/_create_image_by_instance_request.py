# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateImageByInstanceRequest(DaraModel):
    def __init__(
        self,
        auto_clean_userdata: bool = None,
        biz_type: int = None,
        description: str = None,
        disk_type: str = None,
        image_name: str = None,
        instance_id: str = None,
        instance_type: str = None,
        product_type: str = None,
        sub_instance_id: str = None,
    ):
        # This parameter is applicable only to scenarios in which the instance type is Cloud Desktop. Specifies whether to clear private data of users. If this parameter is set to true, the created image clears data in directories other than Administrator and Public in the C:\\Users directory.
        # 
        # Valid values:
        # 
        # *   true: cleanup.
        # *   false: does not clear.
        self.auto_clean_userdata = auto_clean_userdata
        # This parameter is not publicly available.
        self.biz_type = biz_type
        # The description of the image.
        self.description = description
        # The type of disk data contained in the image. By default, the system disk and data disk of the instance are included.
        # 
        # Valid values:
        # 
        # *   SYSTEM: only system disk.
        # *   ALL: system disk + data disk
        self.disk_type = disk_type
        # The name of the image.
        self.image_name = image_name
        # The ID of the RDS instance. The instance can be a CloudDesktop instance, a workstation instance. To ensure data consistency in the image, we recommend that you shut down the instance before you create an image.
        self.instance_id = instance_id
        # The instance type.
        # 
        # Valid values:
        # 
        # *   CloudDesktop: Cloud Desktop.
        # *   WuyingServer: Workstation
        self.instance_type = instance_type
        # This parameter is not publicly available.
        self.product_type = product_type
        # The ID of the child instance. This parameter is not used in cloud computing scenarios. Workstation scenarios, you need to specify a persistent session ID to ensure that a specific instance is located.
        self.sub_instance_id = sub_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_clean_userdata is not None:
            result['AutoCleanUserdata'] = self.auto_clean_userdata

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.description is not None:
            result['Description'] = self.description

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.sub_instance_id is not None:
            result['SubInstanceId'] = self.sub_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCleanUserdata') is not None:
            self.auto_clean_userdata = m.get('AutoCleanUserdata')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('SubInstanceId') is not None:
            self.sub_instance_id = m.get('SubInstanceId')

        return self

