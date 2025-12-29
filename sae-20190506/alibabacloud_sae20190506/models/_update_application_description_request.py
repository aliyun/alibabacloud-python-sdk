# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateApplicationDescriptionRequest(DaraModel):
    def __init__(
        self,
        app_description: str = None,
        app_id: str = None,
    ):
        # The new description of the application. The description can be up to 1,024 characters in length.
        # 
        # This parameter is required.
        self.app_description = app_description
        # The ID of the application that you want to update.
        # 
        # This parameter is required.
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_description is not None:
            result['AppDescription'] = self.app_description

        if self.app_id is not None:
            result['AppId'] = self.app_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppDescription') is not None:
            self.app_description = m.get('AppDescription')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        return self

