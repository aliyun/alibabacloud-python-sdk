# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunScriptPlanningRequest(DaraModel):
    def __init__(
        self,
        additional_note: str = None,
        dialogue_in_scene: bool = None,
        plot_conflict: bool = None,
        script_name: str = None,
        script_shot_count: int = None,
        script_summary: str = None,
        script_type_keyword: str = None,
    ):
        self.additional_note = additional_note
        self.dialogue_in_scene = dialogue_in_scene
        self.plot_conflict = plot_conflict
        self.script_name = script_name
        self.script_shot_count = script_shot_count
        # This parameter is required.
        self.script_summary = script_summary
        self.script_type_keyword = script_type_keyword

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_note is not None:
            result['additionalNote'] = self.additional_note

        if self.dialogue_in_scene is not None:
            result['dialogueInScene'] = self.dialogue_in_scene

        if self.plot_conflict is not None:
            result['plotConflict'] = self.plot_conflict

        if self.script_name is not None:
            result['scriptName'] = self.script_name

        if self.script_shot_count is not None:
            result['scriptShotCount'] = self.script_shot_count

        if self.script_summary is not None:
            result['scriptSummary'] = self.script_summary

        if self.script_type_keyword is not None:
            result['scriptTypeKeyword'] = self.script_type_keyword

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('additionalNote') is not None:
            self.additional_note = m.get('additionalNote')

        if m.get('dialogueInScene') is not None:
            self.dialogue_in_scene = m.get('dialogueInScene')

        if m.get('plotConflict') is not None:
            self.plot_conflict = m.get('plotConflict')

        if m.get('scriptName') is not None:
            self.script_name = m.get('scriptName')

        if m.get('scriptShotCount') is not None:
            self.script_shot_count = m.get('scriptShotCount')

        if m.get('scriptSummary') is not None:
            self.script_summary = m.get('scriptSummary')

        if m.get('scriptTypeKeyword') is not None:
            self.script_type_keyword = m.get('scriptTypeKeyword')

        return self

