# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEdgeContainerAppVersionShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        containers_shrink: str = None,
        name: str = None,
        remarks: str = None,
    ):
        # The application ID. You can call the [ListEdgeContainerApps](~~ListEdgeContainerApps~~) operation to obtain the application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The container group to deploy for this version, including specific image information. The image information consists of the image address, startup commands, parameters, environment variables, and probe rules. Multiple images are supported. This parameter is a JSON array.
        # 
        # This parameter is required.
        self.containers_shrink = containers_shrink
        # The version name. The name must be **6 to 128** characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The remarks.
        self.remarks = remarks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.containers_shrink is not None:
            result['Containers'] = self.containers_shrink

        if self.name is not None:
            result['Name'] = self.name

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Containers') is not None:
            self.containers_shrink = m.get('Containers')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        return self

