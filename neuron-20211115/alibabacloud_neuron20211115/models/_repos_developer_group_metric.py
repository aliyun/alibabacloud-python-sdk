# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReposDeveloperGroupMetric(DaraModel):
    def __init__(
        self,
        add_lines: int = None,
        comment_lines: int = None,
        commit_cnt: int = None,
        del_lines: int = None,
        mod_lines: int = None,
        show_name: str = None,
        work_no: str = None,
    ):
        self.add_lines = add_lines
        self.comment_lines = comment_lines
        self.commit_cnt = commit_cnt
        self.del_lines = del_lines
        self.mod_lines = mod_lines
        self.show_name = show_name
        self.work_no = work_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_lines is not None:
            result['addLines'] = self.add_lines

        if self.comment_lines is not None:
            result['commentLines'] = self.comment_lines

        if self.commit_cnt is not None:
            result['commitCnt'] = self.commit_cnt

        if self.del_lines is not None:
            result['delLines'] = self.del_lines

        if self.mod_lines is not None:
            result['modLines'] = self.mod_lines

        if self.show_name is not None:
            result['showName'] = self.show_name

        if self.work_no is not None:
            result['workNo'] = self.work_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('addLines') is not None:
            self.add_lines = m.get('addLines')

        if m.get('commentLines') is not None:
            self.comment_lines = m.get('commentLines')

        if m.get('commitCnt') is not None:
            self.commit_cnt = m.get('commitCnt')

        if m.get('delLines') is not None:
            self.del_lines = m.get('delLines')

        if m.get('modLines') is not None:
            self.mod_lines = m.get('modLines')

        if m.get('showName') is not None:
            self.show_name = m.get('showName')

        if m.get('workNo') is not None:
            self.work_no = m.get('workNo')

        return self

