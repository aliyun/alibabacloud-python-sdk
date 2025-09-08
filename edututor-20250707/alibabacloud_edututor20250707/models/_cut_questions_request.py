# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edututor20250707 import models as main_models
from darabonba.model import DaraModel

class CutQuestionsRequest(DaraModel):
    def __init__(
        self,
        image: str = None,
        parameters: main_models.CutQuestionsRequestParameters = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.image = image
        # This parameter is required.
        self.parameters = parameters
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['image'] = self.image

        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('parameters') is not None:
            temp_model = main_models.CutQuestionsRequestParameters()
            self.parameters = temp_model.from_map(m.get('parameters'))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class CutQuestionsRequestParameters(DaraModel):
    def __init__(
        self,
        extract_images: bool = None,
        struct: bool = None,
    ):
        # This parameter is required.
        self.extract_images = extract_images
        # This parameter is required.
        self.struct = struct

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extract_images is not None:
            result['extract_images'] = self.extract_images

        if self.struct is not None:
            result['struct'] = self.struct

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extract_images') is not None:
            self.extract_images = m.get('extract_images')

        if m.get('struct') is not None:
            self.struct = m.get('struct')

        return self

