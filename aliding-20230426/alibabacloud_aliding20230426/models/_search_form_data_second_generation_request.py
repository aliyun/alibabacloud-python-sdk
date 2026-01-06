# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchFormDataSecondGenerationRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        create_from_time_gmt: str = None,
        create_to_time_gmt: str = None,
        form_uuid: str = None,
        modified_from_time_gmt: str = None,
        modified_to_time_gmt: str = None,
        order_config_json: str = None,
        originator_id: str = None,
        page_number: int = None,
        page_size: int = None,
        search_condition: str = None,
        system_token: str = None,
    ):
        # This parameter is required.
        self.app_type = app_type
        self.create_from_time_gmt = create_from_time_gmt
        self.create_to_time_gmt = create_to_time_gmt
        # This parameter is required.
        self.form_uuid = form_uuid
        self.modified_from_time_gmt = modified_from_time_gmt
        self.modified_to_time_gmt = modified_to_time_gmt
        self.order_config_json = order_config_json
        self.originator_id = originator_id
        self.page_number = page_number
        self.page_size = page_size
        self.search_condition = search_condition
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

        if self.create_from_time_gmt is not None:
            result['CreateFromTimeGMT'] = self.create_from_time_gmt

        if self.create_to_time_gmt is not None:
            result['CreateToTimeGMT'] = self.create_to_time_gmt

        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.modified_from_time_gmt is not None:
            result['ModifiedFromTimeGMT'] = self.modified_from_time_gmt

        if self.modified_to_time_gmt is not None:
            result['ModifiedToTimeGMT'] = self.modified_to_time_gmt

        if self.order_config_json is not None:
            result['OrderConfigJson'] = self.order_config_json

        if self.originator_id is not None:
            result['OriginatorId'] = self.originator_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_condition is not None:
            result['SearchCondition'] = self.search_condition

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

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

        if m.get('ModifiedFromTimeGMT') is not None:
            self.modified_from_time_gmt = m.get('ModifiedFromTimeGMT')

        if m.get('ModifiedToTimeGMT') is not None:
            self.modified_to_time_gmt = m.get('ModifiedToTimeGMT')

        if m.get('OrderConfigJson') is not None:
            self.order_config_json = m.get('OrderConfigJson')

        if m.get('OriginatorId') is not None:
            self.originator_id = m.get('OriginatorId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchCondition') is not None:
            self.search_condition = m.get('SearchCondition')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        return self

