# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePictureSearchAppRequest(DaraModel):
    def __init__(
        self,
        desc: str = None,
        iot_instance_id: str = None,
        name: str = None,
    ):
        # The description of the image search application instance.
        # 
        # The description can contain Chinese characters, uppercase and lowercase English letters, digits, underscores (_), and hyphens (-). It can be up to 1,024 characters in length, and each Chinese character counts as two characters.
        # 
        # This parameter is required.
        self.desc = desc
        # The instance ID.
        # 
        # You can view the **ID** of the current instance on the **Instance Overview** page in the IoT Platform console. If the instance has an ID, you must specify this ID. Otherwise, the call fails.
        # 
        # > If the public instance does not have an ID, see [How to obtain an instance ID](https://help.aliyun.com/document_detail/267533.html).
        self.iot_instance_id = iot_instance_id
        # The name of the image search application instance. 
        # 
        # The name can contain Chinese characters, uppercase and lowercase English letters, digits, underscores (_), and hyphens (-). It can be up to 64 characters in length, and each Chinese character counts as two characters.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

