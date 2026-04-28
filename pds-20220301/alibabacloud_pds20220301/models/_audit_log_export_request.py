# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuditLogExportRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        language: str = None,
        order_by: str = None,
        query: str = None,
    ):
        # The name of the exported file. The name can be up to 1,024 characters in length. The default name suffix is log.csv.
        self.file_name = file_name
        # The export language. Default value: zh-CN. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en_US: English
        self.language = language
        # The sort order based on the operation time. If you leave this parameter empty, the value acted_at DESC is used. Valid values:
        # 
        # *   acted_at DESC: sorts the entries by operation time in descending order
        # *   acted_at ASC: sorts the entries by operation time in ascending order
        self.order_by = order_by
        # The fields used for query. You can specify one or more of the following fields:
        # 
        # *   drive_id (space ID, in the form of a string)
        # *   actor_id (operator ID, in the form of a string)
        # *   acted_at (operation time, in the yyyy-MM-ddTHH:mm:ssZ format in UTC, for example, 2006-01-02T00:00:00)
        # *   action_type (operation type, in the form of a string)
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['file_name'] = self.file_name

        if self.language is not None:
            result['language'] = self.language

        if self.order_by is not None:
            result['order_by'] = self.order_by

        if self.query is not None:
            result['query'] = self.query

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')

        if m.get('query') is not None:
            self.query = m.get('query')

        return self

