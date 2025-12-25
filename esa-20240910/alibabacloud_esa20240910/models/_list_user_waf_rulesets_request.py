# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListUserWafRulesetsRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        phase: str = None,
        query_args: main_models.ListUserWafRulesetsRequestQueryArgs = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.phase = phase
        self.query_args = query_args

    def validate(self):
        if self.query_args:
            self.query_args.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.query_args is not None:
            result['QueryArgs'] = self.query_args.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('QueryArgs') is not None:
            temp_model = main_models.ListUserWafRulesetsRequestQueryArgs()
            self.query_args = temp_model.from_map(m.get('QueryArgs'))

        return self

class ListUserWafRulesetsRequestQueryArgs(DaraModel):
    def __init__(
        self,
        desc: bool = None,
        name_like: str = None,
        order_by: str = None,
    ):
        self.desc = desc
        self.name_like = name_like
        self.order_by = order_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.name_like is not None:
            result['NameLike'] = self.name_like

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('NameLike') is not None:
            self.name_like = m.get('NameLike')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        return self

