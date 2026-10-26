# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDataMaskingRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        engine_type: str = None,
        instance_id: str = None,
        lang: str = None,
        product_code: str = None,
        product_id: int = None,
        sub_rule_list_shrink: str = None,
    ):
        # The database engine type. The value must be the same as the EngineType of the target instance, such as MySQL or PostgreSQL.
        self.engine_type = engine_type
        # The database instance identifier. You can obtain this value from the Items[].InstanceId field in the response of the ListDataMaskingInstances operation.
        self.instance_id = instance_id
        # The language of the response message. Valid values: zh: Chinese. en: English.
        self.lang = lang
        # The cloud service code. Column encryption supports RDS, POLARDB, and PolarDBX2. If ProductId is also specified, the two parameters must match.
        self.product_code = product_code
        # The cloud service type identifier. Valid values: 5: RDS. 8: POLARDB. 27: PolarDBX2. If this parameter is specified together with ProductCode, the values must match.
        self.product_id = product_id
        # The list of column encryption targets grouped by database and table.
        self.sub_rule_list_shrink = sub_rule_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.sub_rule_list_shrink is not None:
            result['SubRuleList'] = self.sub_rule_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('SubRuleList') is not None:
            self.sub_rule_list_shrink = m.get('SubRuleList')

        return self

