# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class Lifecycle(DaraModel):
    def __init__(
        self,
        post_start: main_models.LifecyclePostStart = None,
        pre_stop: main_models.LifecyclePreStop = None,
    ):
        self.post_start = post_start
        self.pre_stop = pre_stop

    def validate(self):
        if self.post_start:
            self.post_start.validate()
        if self.pre_stop:
            self.pre_stop.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.post_start is not None:
            result['PostStart'] = self.post_start.to_map()

        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PostStart') is not None:
            temp_model = main_models.LifecyclePostStart()
            self.post_start = temp_model.from_map(m.get('PostStart'))

        if m.get('PreStop') is not None:
            temp_model = main_models.LifecyclePreStop()
            self.pre_stop = temp_model.from_map(m.get('PreStop'))

        return self

class LifecyclePreStop(DaraModel):
    def __init__(
        self,
        exec: main_models.LifecyclePreStopExec = None,
    ):
        self.exec = exec

    def validate(self):
        if self.exec:
            self.exec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = main_models.LifecyclePreStopExec()
            self.exec = temp_model.from_map(m.get('Exec'))

        return self

class LifecyclePreStopExec(DaraModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')

        return self

class LifecyclePostStart(DaraModel):
    def __init__(
        self,
        exec: main_models.LifecyclePostStartExec = None,
    ):
        self.exec = exec

    def validate(self):
        if self.exec:
            self.exec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = main_models.LifecyclePostStartExec()
            self.exec = temp_model.from_map(m.get('Exec'))

        return self

class LifecyclePostStartExec(DaraModel):
    def __init__(
        self,
        command: List[str] = None,
    ):
        self.command = command

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.command is not None:
            result['Command'] = self.command

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')

        return self

