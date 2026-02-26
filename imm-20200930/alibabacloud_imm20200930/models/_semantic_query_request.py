# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SemanticQueryRequest(DaraModel):
    def __init__(
        self,
        dataset_name: str = None,
        max_results: int = None,
        media_types: List[str] = None,
        next_token: str = None,
        project_name: str = None,
        query: str = None,
        source_uri: str = None,
        with_fields: List[str] = None,
    ):
        # The name of the dataset.
        # 
        # This parameter is required.
        self.dataset_name = dataset_name
        # The maximum number of entries to return. Valid values: 1 to 1000.
        self.max_results = max_results
        # The types of the media that you want to query. Default value:
        # 
        # ["image"]
        self.media_types = media_types
        # This parameter is no longer available.
        self.next_token = next_token
        # The name of the project.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The content of the query that you input.
        self.query = query
        # > Either this parameter or the Query parameter must be specified. This parameter is valid only for image searches on datasets configured with a search-by-image workflow.
        # >
        # URI of the source data for retrieval.
        # The URI must be in the oss://${Bucket}/${Object} format. ${Bucket} specifies the name of the OSS bucket that is in the same region as the current project. ${Object} specifies the full path of the file that contains the file name extension.
        # 
        # Contact us if you need to configure a workflow template.
        self.source_uri = source_uri
        # >  Either this parameter or the SourceURI parameter must be specified.
        # 
        # The content of the query that you input.
        self.with_fields = with_fields

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.media_types is not None:
            result['MediaTypes'] = self.media_types

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.query is not None:
            result['Query'] = self.query

        if self.source_uri is not None:
            result['SourceURI'] = self.source_uri

        if self.with_fields is not None:
            result['WithFields'] = self.with_fields

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('MediaTypes') is not None:
            self.media_types = m.get('MediaTypes')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('SourceURI') is not None:
            self.source_uri = m.get('SourceURI')

        if m.get('WithFields') is not None:
            self.with_fields = m.get('WithFields')

        return self

