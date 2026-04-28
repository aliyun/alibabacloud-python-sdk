# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReportBizAlertInfoShrinkRequest(DaraModel):
    def __init__(
        self,
        alert_description: str = None,
        alert_detail: str = None,
        alert_grade: str = None,
        alert_labels: str = None,
        alert_scene: str = None,
        alert_token: str = None,
        alert_uid_shrink: str = None,
        language: str = None,
    ):
        self.alert_description = alert_description
        # This parameter is required.
        self.alert_detail = alert_detail
        self.alert_grade = alert_grade
        self.alert_labels = alert_labels
        # This parameter is required.
        self.alert_scene = alert_scene
        # This parameter is required.
        self.alert_token = alert_token
        self.alert_uid_shrink = alert_uid_shrink
        self.language = language

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_description is not None:
            result['AlertDescription'] = self.alert_description

        if self.alert_detail is not None:
            result['AlertDetail'] = self.alert_detail

        if self.alert_grade is not None:
            result['AlertGrade'] = self.alert_grade

        if self.alert_labels is not None:
            result['AlertLabels'] = self.alert_labels

        if self.alert_scene is not None:
            result['AlertScene'] = self.alert_scene

        if self.alert_token is not None:
            result['AlertToken'] = self.alert_token

        if self.alert_uid_shrink is not None:
            result['AlertUid'] = self.alert_uid_shrink

        if self.language is not None:
            result['Language'] = self.language

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertDescription') is not None:
            self.alert_description = m.get('AlertDescription')

        if m.get('AlertDetail') is not None:
            self.alert_detail = m.get('AlertDetail')

        if m.get('AlertGrade') is not None:
            self.alert_grade = m.get('AlertGrade')

        if m.get('AlertLabels') is not None:
            self.alert_labels = m.get('AlertLabels')

        if m.get('AlertScene') is not None:
            self.alert_scene = m.get('AlertScene')

        if m.get('AlertToken') is not None:
            self.alert_token = m.get('AlertToken')

        if m.get('AlertUid') is not None:
            self.alert_uid_shrink = m.get('AlertUid')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        return self

