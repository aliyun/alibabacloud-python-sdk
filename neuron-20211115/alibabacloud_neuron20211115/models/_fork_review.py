# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ForkReview(DaraModel):
    def __init__(
        self,
        applicant: str = None,
        fork_id: int = None,
        git_group: str = None,
        id: int = None,
        pbc_name: str = None,
        repo_urls: List[str] = None,
        request_id: str = None,
        reviewer: str = None,
        reviewer_id: str = None,
        status: str = None,
        usage: str = None,
    ):
        self.applicant = applicant
        self.fork_id = fork_id
        self.git_group = git_group
        self.id = id
        self.pbc_name = pbc_name
        self.repo_urls = repo_urls
        self.request_id = request_id
        self.reviewer = reviewer
        self.reviewer_id = reviewer_id
        self.status = status
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.applicant is not None:
            result['applicant'] = self.applicant

        if self.fork_id is not None:
            result['forkId'] = self.fork_id

        if self.git_group is not None:
            result['gitGroup'] = self.git_group

        if self.id is not None:
            result['id'] = self.id

        if self.pbc_name is not None:
            result['pbcName'] = self.pbc_name

        if self.repo_urls is not None:
            result['repoUrls'] = self.repo_urls

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.reviewer is not None:
            result['reviewer'] = self.reviewer

        if self.reviewer_id is not None:
            result['reviewerId'] = self.reviewer_id

        if self.status is not None:
            result['status'] = self.status

        if self.usage is not None:
            result['usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('applicant') is not None:
            self.applicant = m.get('applicant')

        if m.get('forkId') is not None:
            self.fork_id = m.get('forkId')

        if m.get('gitGroup') is not None:
            self.git_group = m.get('gitGroup')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('pbcName') is not None:
            self.pbc_name = m.get('pbcName')

        if m.get('repoUrls') is not None:
            self.repo_urls = m.get('repoUrls')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('reviewer') is not None:
            self.reviewer = m.get('reviewer')

        if m.get('reviewerId') is not None:
            self.reviewer_id = m.get('reviewerId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('usage') is not None:
            self.usage = m.get('usage')

        return self

