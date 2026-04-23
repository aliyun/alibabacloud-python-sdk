# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class KnowledgeJobInfoVO(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        creator: str = None,
        description: str = None,
        end_time: str = None,
        job_id: int = None,
        knowledge_cnt: int = None,
        progress: int = None,
        show_job_id: str = None,
        status: str = None,
        supplement: str = None,
        table_cnt: int = None,
    ):
        self.create_time = create_time
        self.creator = creator
        self.description = description
        self.end_time = end_time
        self.job_id = job_id
        self.knowledge_cnt = knowledge_cnt
        self.progress = progress
        self.show_job_id = show_job_id
        self.status = status
        self.supplement = supplement
        self.table_cnt = table_cnt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.knowledge_cnt is not None:
            result['KnowledgeCnt'] = self.knowledge_cnt

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.show_job_id is not None:
            result['ShowJobId'] = self.show_job_id

        if self.status is not None:
            result['Status'] = self.status

        if self.supplement is not None:
            result['Supplement'] = self.supplement

        if self.table_cnt is not None:
            result['TableCnt'] = self.table_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('KnowledgeCnt') is not None:
            self.knowledge_cnt = m.get('KnowledgeCnt')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ShowJobId') is not None:
            self.show_job_id = m.get('ShowJobId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Supplement') is not None:
            self.supplement = m.get('Supplement')

        if m.get('TableCnt') is not None:
            self.table_cnt = m.get('TableCnt')

        return self

