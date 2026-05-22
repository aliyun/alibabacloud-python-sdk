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
        # The application ID, which can be obtained by calling the [ListEdgeContainerApps](~~ListEdgeContainerApps~~) operation.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The container group to be deployed for this version, which contains information about images.\\
        # The image data contains the image address, startup command, parameters, environment variables, and probe rules. You can specify one or more images. The parameter value is a JSON string.
        # 
        # This parameter is required.
        self.containers_shrink = containers_shrink
        # The version name, which must be 6 to 128 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The description of the version.
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

