# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchEmployeeFieldValuesRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        create_from_time_gmt: str = None,
        create_to_time_gmt: str = None,
        form_uuid: str = None,
        language: str = None,
        modified_from_time_gmt: str = None,
        modified_to_time_gmt: str = None,
        originator_id: str = None,
        search_field_json: str = None,
        system_token: str = None,
        target_field_json: str = None,
    ):
        self.app_type = app_type
        self.create_from_time_gmt = create_from_time_gmt
        self.create_to_time_gmt = create_to_time_gmt
        self.form_uuid = form_uuid
        self.language = language
        self.modified_from_time_gmt = modified_from_time_gmt
        self.modified_to_time_gmt = modified_to_time_gmt
        self.originator_id = originator_id
        self.search_field_json = search_field_json
        self.system_token = system_token
        self.target_field_json = target_field_json

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.create_from_time_gmt is not None:
            result['CreateFromTimeGMT'] = self.create_from_time_gmt

        if self.create_to_time_gmt is not None:
            result['CreateToTimeGMT'] = self.create_to_time_gmt

        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.language is not None:
            result['Language'] = self.language

        if self.modified_from_time_gmt is not None:
            result['ModifiedFromTimeGMT'] = self.modified_from_time_gmt

        if self.modified_to_time_gmt is not None:
            result['ModifiedToTimeGMT'] = self.modified_to_time_gmt

        if self.originator_id is not None:
            result['OriginatorId'] = self.originator_id

        if self.search_field_json is not None:
            result['SearchFieldJson'] = self.search_field_json

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        if self.target_field_json is not None:
            result['TargetFieldJson'] = self.target_field_json

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('CreateFromTimeGMT') is not None:
            self.create_from_time_gmt = m.get('CreateFromTimeGMT')

        if m.get('CreateToTimeGMT') is not None:
            self.create_to_time_gmt = m.get('CreateToTimeGMT')

        if m.get('FormUuid') is not None:
            self.form_uuid = m.get('FormUuid')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('ModifiedFromTimeGMT') is not None:
            self.modified_from_time_gmt = m.get('ModifiedFromTimeGMT')

        if m.get('ModifiedToTimeGMT') is not None:
            self.modified_to_time_gmt = m.get('ModifiedToTimeGMT')

        if m.get('OriginatorId') is not None:
            self.originator_id = m.get('OriginatorId')

        if m.get('SearchFieldJson') is not None:
            self.search_field_json = m.get('SearchFieldJson')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        if m.get('TargetFieldJson') is not None:
            self.target_field_json = m.get('TargetFieldJson')

        return self

