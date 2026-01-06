# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class Filters(DaraModel):
    def __init__(
        self,
        app_id_regex: str = None,
        app_name_regex: str = None,
        app_state: str = None,
        app_type: str = None,
        execution_time_range: main_models.FiltersExecutionTimeRange = None,
        submit_time_range: main_models.FiltersSubmitTimeRange = None,
        termiated_time_range: main_models.FiltersTermiatedTimeRange = None,
    ):
        self.app_id_regex = app_id_regex
        self.app_name_regex = app_name_regex
        self.app_state = app_state
        self.app_type = app_type
        self.execution_time_range = execution_time_range
        self.submit_time_range = submit_time_range
        self.termiated_time_range = termiated_time_range

    def validate(self):
        if self.execution_time_range:
            self.execution_time_range.validate()
        if self.submit_time_range:
            self.submit_time_range.validate()
        if self.termiated_time_range:
            self.termiated_time_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id_regex is not None:
            result['AppIdRegex'] = self.app_id_regex

        if self.app_name_regex is not None:
            result['AppNameRegex'] = self.app_name_regex

        if self.app_state is not None:
            result['AppState'] = self.app_state

        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.execution_time_range is not None:
            result['ExecutionTimeRange'] = self.execution_time_range.to_map()

        if self.submit_time_range is not None:
            result['SubmitTimeRange'] = self.submit_time_range.to_map()

        if self.termiated_time_range is not None:
            result['TermiatedTimeRange'] = self.termiated_time_range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdRegex') is not None:
            self.app_id_regex = m.get('AppIdRegex')

        if m.get('AppNameRegex') is not None:
            self.app_name_regex = m.get('AppNameRegex')

        if m.get('AppState') is not None:
            self.app_state = m.get('AppState')

        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('ExecutionTimeRange') is not None:
            temp_model = main_models.FiltersExecutionTimeRange()
            self.execution_time_range = temp_model.from_map(m.get('ExecutionTimeRange'))

        if m.get('SubmitTimeRange') is not None:
            temp_model = main_models.FiltersSubmitTimeRange()
            self.submit_time_range = temp_model.from_map(m.get('SubmitTimeRange'))

        if m.get('TermiatedTimeRange') is not None:
            temp_model = main_models.FiltersTermiatedTimeRange()
            self.termiated_time_range = temp_model.from_map(m.get('TermiatedTimeRange'))

        return self

class FiltersTermiatedTimeRange(DaraModel):
    def __init__(
        self,
        max_time_in_mills: int = None,
        min_time_in_mills: int = None,
    ):
        self.max_time_in_mills = max_time_in_mills
        self.min_time_in_mills = min_time_in_mills

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_time_in_mills is not None:
            result['MaxTimeInMills'] = self.max_time_in_mills

        if self.min_time_in_mills is not None:
            result['MinTimeInMills'] = self.min_time_in_mills

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxTimeInMills') is not None:
            self.max_time_in_mills = m.get('MaxTimeInMills')

        if m.get('MinTimeInMills') is not None:
            self.min_time_in_mills = m.get('MinTimeInMills')

        return self

class FiltersSubmitTimeRange(DaraModel):
    def __init__(
        self,
        max_time_in_mills: int = None,
        min_time_in_mills: int = None,
    ):
        self.max_time_in_mills = max_time_in_mills
        self.min_time_in_mills = min_time_in_mills

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_time_in_mills is not None:
            result['MaxTimeInMills'] = self.max_time_in_mills

        if self.min_time_in_mills is not None:
            result['MinTimeInMills'] = self.min_time_in_mills

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxTimeInMills') is not None:
            self.max_time_in_mills = m.get('MaxTimeInMills')

        if m.get('MinTimeInMills') is not None:
            self.min_time_in_mills = m.get('MinTimeInMills')

        return self



class FiltersExecutionTimeRange(DaraModel):
    def __init__(
        self,
        max_time_in_seconds: int = None,
        min_time_in_seconds: int = None,
    ):
        self.max_time_in_seconds = max_time_in_seconds
        self.min_time_in_seconds = min_time_in_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_time_in_seconds is not None:
            result['MaxTimeInSeconds'] = self.max_time_in_seconds

        if self.min_time_in_seconds is not None:
            result['MinTimeInSeconds'] = self.min_time_in_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxTimeInSeconds') is not None:
            self.max_time_in_seconds = m.get('MaxTimeInSeconds')

        if m.get('MinTimeInSeconds') is not None:
            self.min_time_in_seconds = m.get('MinTimeInSeconds')

        return self

