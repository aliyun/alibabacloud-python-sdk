# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class Artifact(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        catagory_biz_id: str = None,
        creator: int = None,
        credential: main_models.Credential = None,
        full_path: List[str] = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        location: str = None,
        modifier: int = None,
        modifier_name: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.biz_id = biz_id
        self.catagory_biz_id = catagory_biz_id
        # This parameter is required.
        self.creator = creator
        self.credential = credential
        self.full_path = full_path
        # This parameter is required.
        self.gmt_created = gmt_created
        # This parameter is required.
        self.gmt_modified = gmt_modified
        # This parameter is required.
        self.location = location
        # This parameter is required.
        self.modifier = modifier
        self.modifier_name = modifier_name
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.credential:
            self.credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['bizId'] = self.biz_id

        if self.catagory_biz_id is not None:
            result['catagoryBizId'] = self.catagory_biz_id

        if self.creator is not None:
            result['creator'] = self.creator

        if self.credential is not None:
            result['credential'] = self.credential.to_map()

        if self.full_path is not None:
            result['fullPath'] = self.full_path

        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.location is not None:
            result['location'] = self.location

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')

        if m.get('catagoryBizId') is not None:
            self.catagory_biz_id = m.get('catagoryBizId')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('credential') is not None:
            temp_model = main_models.Credential()
            self.credential = temp_model.from_map(m.get('credential'))

        if m.get('fullPath') is not None:
            self.full_path = m.get('fullPath')

        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('location') is not None:
            self.location = m.get('location')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

