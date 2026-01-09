# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryAiCallDetailPageRequest(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        call_result: str = None,
        called_number: str = None,
        detail_ids: List[int] = None,
        end_calling_time: int = None,
        end_imported_time: int = None,
        major_intent: str = None,
        max_conversation_duration: int = None,
        min_conversation_duration: int = None,
        out_id: str = None,
        owner_id: int = None,
        page_no: int = None,
        page_size: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        start_calling_time: int = None,
        start_imported_time: int = None,
        status: int = None,
        task_id: str = None,
    ):
        self.batch_id = batch_id
        self.call_result = call_result
        self.called_number = called_number
        self.detail_ids = detail_ids
        self.end_calling_time = end_calling_time
        self.end_imported_time = end_imported_time
        self.major_intent = major_intent
        self.max_conversation_duration = max_conversation_duration
        self.min_conversation_duration = min_conversation_duration
        self.out_id = out_id
        self.owner_id = owner_id
        self.page_no = page_no
        self.page_size = page_size
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        self.start_calling_time = start_calling_time
        self.start_imported_time = start_imported_time
        # This parameter is required.
        self.status = status
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.call_result is not None:
            result['CallResult'] = self.call_result

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.detail_ids is not None:
            result['DetailIds'] = self.detail_ids

        if self.end_calling_time is not None:
            result['EndCallingTime'] = self.end_calling_time

        if self.end_imported_time is not None:
            result['EndImportedTime'] = self.end_imported_time

        if self.major_intent is not None:
            result['MajorIntent'] = self.major_intent

        if self.max_conversation_duration is not None:
            result['MaxConversationDuration'] = self.max_conversation_duration

        if self.min_conversation_duration is not None:
            result['MinConversationDuration'] = self.min_conversation_duration

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.start_calling_time is not None:
            result['StartCallingTime'] = self.start_calling_time

        if self.start_imported_time is not None:
            result['StartImportedTime'] = self.start_imported_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('DetailIds') is not None:
            self.detail_ids = m.get('DetailIds')

        if m.get('EndCallingTime') is not None:
            self.end_calling_time = m.get('EndCallingTime')

        if m.get('EndImportedTime') is not None:
            self.end_imported_time = m.get('EndImportedTime')

        if m.get('MajorIntent') is not None:
            self.major_intent = m.get('MajorIntent')

        if m.get('MaxConversationDuration') is not None:
            self.max_conversation_duration = m.get('MaxConversationDuration')

        if m.get('MinConversationDuration') is not None:
            self.min_conversation_duration = m.get('MinConversationDuration')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('StartCallingTime') is not None:
            self.start_calling_time = m.get('StartCallingTime')

        if m.get('StartImportedTime') is not None:
            self.start_imported_time = m.get('StartImportedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

