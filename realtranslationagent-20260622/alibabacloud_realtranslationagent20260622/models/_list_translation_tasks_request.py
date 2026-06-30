# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTranslationTasksRequest(DaraModel):
    def __init__(
        self,
        apikey: str = None,
        end_time: str = None,
        max_results: int = None,
        next_token: str = None,
        original_file_name: str = None,
        source_language: str = None,
        start_time: str = None,
        status: str = None,
        target_language: str = None,
        task_id: str = None,
    ):
        self.apikey = apikey
        self.end_time = end_time
        self.max_results = max_results
        self.next_token = next_token
        self.original_file_name = original_file_name
        self.source_language = source_language
        self.start_time = start_time
        self.status = status
        self.target_language = target_language
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apikey is not None:
            result['APIKey'] = self.apikey

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.original_file_name is not None:
            result['OriginalFileName'] = self.original_file_name

        if self.source_language is not None:
            result['SourceLanguage'] = self.source_language

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.target_language is not None:
            result['TargetLanguage'] = self.target_language

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('APIKey') is not None:
            self.apikey = m.get('APIKey')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OriginalFileName') is not None:
            self.original_file_name = m.get('OriginalFileName')

        if m.get('SourceLanguage') is not None:
            self.source_language = m.get('SourceLanguage')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetLanguage') is not None:
            self.target_language = m.get('TargetLanguage')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

