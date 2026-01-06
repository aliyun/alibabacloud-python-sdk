# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class BatchGetFormDataByIdListRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        form_instance_id_list: List[str] = None,
        form_uuid: str = None,
        need_form_instance_value: bool = None,
        system_token: str = None,
    ):
        # This parameter is required.
        self.app_type = app_type
        # This parameter is required.
        self.form_instance_id_list = form_instance_id_list
        # This parameter is required.
        self.form_uuid = form_uuid
        self.need_form_instance_value = need_form_instance_value
        # This parameter is required.
        self.system_token = system_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.form_instance_id_list is not None:
            result['FormInstanceIdList'] = self.form_instance_id_list

        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.need_form_instance_value is not None:
            result['NeedFormInstanceValue'] = self.need_form_instance_value

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('FormInstanceIdList') is not None:
            self.form_instance_id_list = m.get('FormInstanceIdList')

        if m.get('FormUuid') is not None:
            self.form_uuid = m.get('FormUuid')

        if m.get('NeedFormInstanceValue') is not None:
            self.need_form_instance_value = m.get('NeedFormInstanceValue')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        return self

