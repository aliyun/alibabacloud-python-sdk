# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDocumentRetrieveRequest(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        element_scope: str = None,
        end_date: str = None,
        max_results: int = None,
        next_token: str = None,
        office: str = None,
        query: str = None,
        region: str = None,
        source: str = None,
        start_date: str = None,
        sub_content_type: str = None,
        subject_classify: str = None,
        word_size: str = None,
        workspace_id: str = None,
    ):
        self.content_type = content_type
        self.element_scope = element_scope
        self.end_date = end_date
        self.max_results = max_results
        self.next_token = next_token
        self.office = office
        self.query = query
        self.region = region
        self.source = source
        self.start_date = start_date
        self.sub_content_type = sub_content_type
        self.subject_classify = subject_classify
        self.word_size = word_size
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.element_scope is not None:
            result['ElementScope'] = self.element_scope

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.office is not None:
            result['Office'] = self.office

        if self.query is not None:
            result['Query'] = self.query

        if self.region is not None:
            result['Region'] = self.region

        if self.source is not None:
            result['Source'] = self.source

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.sub_content_type is not None:
            result['SubContentType'] = self.sub_content_type

        if self.subject_classify is not None:
            result['SubjectClassify'] = self.subject_classify

        if self.word_size is not None:
            result['WordSize'] = self.word_size

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('ElementScope') is not None:
            self.element_scope = m.get('ElementScope')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Office') is not None:
            self.office = m.get('Office')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('SubContentType') is not None:
            self.sub_content_type = m.get('SubContentType')

        if m.get('SubjectClassify') is not None:
            self.subject_classify = m.get('SubjectClassify')

        if m.get('WordSize') is not None:
            self.word_size = m.get('WordSize')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

