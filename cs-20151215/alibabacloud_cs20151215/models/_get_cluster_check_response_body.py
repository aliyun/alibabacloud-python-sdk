# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List, Any

from darabonba.model import DaraModel

class GetClusterCheckResponseBody(DaraModel):
    def __init__(
        self,
        check_id: str = None,
        check_items: Dict[str, List[Dict[str, Any]]] = None,
        created_at: str = None,
        finished_at: str = None,
        message: str = None,
        status: str = None,
        type: str = None,
    ):
        # The ID of the cluster check task.
        self.check_id = check_id
        # A list of check items.
        self.check_items = check_items
        # The time when the cluster check task was created.
        self.created_at = created_at
        # The time when the cluster check task was completed.
        self.finished_at = finished_at
        # The message that indicates the status of the cluster check task.
        self.message = message
        # The status of the cluster check.
        self.status = status
        # The check method.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['check_id'] = self.check_id

        if self.check_items is not None:
            result['check_items'] = self.check_items

        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.finished_at is not None:
            result['finished_at'] = self.finished_at

        if self.message is not None:
            result['message'] = self.message

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_id') is not None:
            self.check_id = m.get('check_id')

        if m.get('check_items') is not None:
            self.check_items = m.get('check_items')

        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('finished_at') is not None:
            self.finished_at = m.get('finished_at')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

