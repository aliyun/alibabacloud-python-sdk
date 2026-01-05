# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomImageRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        image_name: str = None,
        instance_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. By default, this parameter is left empty. The token cannot exceed 64 characters in length.
        self.client_token = client_token
        # The description of the custom image.
        self.description = description
        # The name of the custom image.
        # 
        # This parameter is required.
        self.image_name = image_name
        # The ID of the cloud phone instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

