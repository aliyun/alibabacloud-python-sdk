# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventVariableListRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        create_type: str = None,
        filter_dto: str = None,
        ref_obj_id: str = None,
        ref_obj_type: str = None,
        reg_id: str = None,
        type: str = None,
    ):
        # Sets the language type for requests and received messages, with a default value of **zh**. The values are: - **zh**: Chinese - **en**: English
        self.lang = lang
        # Create Type.
        self.create_type = create_type
        # Filter object.
        self.filter_dto = filter_dto
        # Associated event eventCode.
        # 
        # This parameter is required.
        self.ref_obj_id = ref_obj_id
        # Association Type.
        # 
        # This parameter is required.
        self.ref_obj_type = ref_obj_type
        # Region Code.
        self.reg_id = reg_id
        # type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.create_type is not None:
            result['createType'] = self.create_type

        if self.filter_dto is not None:
            result['filterDTO'] = self.filter_dto

        if self.ref_obj_id is not None:
            result['refObjId'] = self.ref_obj_id

        if self.ref_obj_type is not None:
            result['refObjType'] = self.ref_obj_type

        if self.reg_id is not None:
            result['regId'] = self.reg_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('createType') is not None:
            self.create_type = m.get('createType')

        if m.get('filterDTO') is not None:
            self.filter_dto = m.get('filterDTO')

        if m.get('refObjId') is not None:
            self.ref_obj_id = m.get('refObjId')

        if m.get('refObjType') is not None:
            self.ref_obj_type = m.get('refObjType')

        if m.get('regId') is not None:
            self.reg_id = m.get('regId')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

