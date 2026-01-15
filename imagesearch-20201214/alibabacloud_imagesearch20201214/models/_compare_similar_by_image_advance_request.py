# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO

from darabonba.model import DaraModel

class CompareSimilarByImageAdvanceRequest(DaraModel):
    def __init__(
        self,
        instance_name: str = None,
        primary_pic_content_object: BinaryIO = None,
        secondary_pic_content_object: BinaryIO = None,
    ):
        # This parameter is required.
        self.instance_name = instance_name
        # This parameter is required.
        self.primary_pic_content_object = primary_pic_content_object
        # This parameter is required.
        self.secondary_pic_content_object = secondary_pic_content_object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.primary_pic_content_object is not None:
            result['PrimaryPicContent'] = self.primary_pic_content_object

        if self.secondary_pic_content_object is not None:
            result['SecondaryPicContent'] = self.secondary_pic_content_object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PrimaryPicContent') is not None:
            self.primary_pic_content_object = m.get('PrimaryPicContent')

        if m.get('SecondaryPicContent') is not None:
            self.secondary_pic_content_object = m.get('SecondaryPicContent')

        return self

