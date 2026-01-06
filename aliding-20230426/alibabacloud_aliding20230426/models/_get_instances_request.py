# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstancesRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        approved_result: str = None,
        create_from_time_gmt: str = None,
        create_to_time_gmt: str = None,
        form_uuid: str = None,
        instance_status: str = None,
        language: str = None,
        modified_from_time_gmt: str = None,
        modified_to_time_gmt: str = None,
        order_config_json: str = None,
        originator_id: str = None,
        page_number: int = None,
        page_size: int = None,
        search_field_json: str = None,
        system_token: str = None,
        task_id: str = None,
    ):
        self.app_type = app_type
        self.approved_result = approved_result
        self.create_from_time_gmt = create_from_time_gmt
        self.create_to_time_gmt = create_to_time_gmt
        self.form_uuid = form_uuid
        self.instance_status = instance_status
        self.language = language
        self.modified_from_time_gmt = modified_from_time_gmt
        self.modified_to_time_gmt = modified_to_time_gmt
        self.order_config_json = order_config_json
        self.originator_id = originator_id
        self.page_number = page_number
        self.page_size = page_size
        self.search_field_json = search_field_json
        self.system_token = system_token
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.approved_result is not None:
            result['ApprovedResult'] = self.approved_result

        if self.create_from_time_gmt is not None:
            result['CreateFromTimeGMT'] = self.create_from_time_gmt

        if self.create_to_time_gmt is not None:
            result['CreateToTimeGMT'] = self.create_to_time_gmt

        if self.form_uuid is not None:
            result['FormUuid'] = self.form_uuid

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.language is not None:
            result['Language'] = self.language

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

        if self.search_field_json is not None:
            result['SearchFieldJson'] = self.search_field_json

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('ApprovedResult') is not None:
            self.approved_result = m.get('ApprovedResult')

        if m.get('CreateFromTimeGMT') is not None:
            self.create_from_time_gmt = m.get('CreateFromTimeGMT')

        if m.get('CreateToTimeGMT') is not None:
            self.create_to_time_gmt = m.get('CreateToTimeGMT')

        if m.get('FormUuid') is not None:
            self.form_uuid = m.get('FormUuid')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('Language') is not None:
            self.language = m.get('Language')

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

        if m.get('SearchFieldJson') is not None:
            self.search_field_json = m.get('SearchFieldJson')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

