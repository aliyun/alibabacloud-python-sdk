# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nas20170626 import models as main_models
from darabonba.model import DaraModel

class DescribeLogAnalysisResponseBody(DaraModel):
    def __init__(
        self,
        analyses: main_models.DescribeLogAnalysisResponseBodyAnalyses = None,
        code: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The collection of log dump information.
        self.analyses = analyses
        # The HTTP status code.
        self.code = code
        # The page number.
        self.page_number = page_number
        # The number of log dump entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of log dump entries in the region.
        self.total_count = total_count

    def validate(self):
        if self.analyses:
            self.analyses.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analyses is not None:
            result['Analyses'] = self.analyses.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Analyses') is not None:
            temp_model = main_models.DescribeLogAnalysisResponseBodyAnalyses()
            self.analyses = temp_model.from_map(m.get('Analyses'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeLogAnalysisResponseBodyAnalyses(DaraModel):
    def __init__(
        self,
        analysis: List[main_models.DescribeLogAnalysisResponseBodyAnalysesAnalysis] = None,
    ):
        self.analysis = analysis

    def validate(self):
        if self.analysis:
            for v1 in self.analysis:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Analysis'] = []
        if self.analysis is not None:
            for k1 in self.analysis:
                result['Analysis'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.analysis = []
        if m.get('Analysis') is not None:
            for k1 in m.get('Analysis'):
                temp_model = main_models.DescribeLogAnalysisResponseBodyAnalysesAnalysis()
                self.analysis.append(temp_model.from_map(k1))

        return self

class DescribeLogAnalysisResponseBodyAnalysesAnalysis(DaraModel):
    def __init__(
        self,
        meta_key: str = None,
        meta_value: main_models.DescribeLogAnalysisResponseBodyAnalysesAnalysisMetaValue = None,
    ):
        # The ID of the file system.
        self.meta_key = meta_key
        # The log dump information of the file system.
        self.meta_value = meta_value

    def validate(self):
        if self.meta_value:
            self.meta_value.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.meta_key is not None:
            result['MetaKey'] = self.meta_key

        if self.meta_value is not None:
            result['MetaValue'] = self.meta_value.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetaKey') is not None:
            self.meta_key = m.get('MetaKey')

        if m.get('MetaValue') is not None:
            temp_model = main_models.DescribeLogAnalysisResponseBodyAnalysesAnalysisMetaValue()
            self.meta_value = temp_model.from_map(m.get('MetaValue'))

        return self

class DescribeLogAnalysisResponseBodyAnalysesAnalysisMetaValue(DaraModel):
    def __init__(
        self,
        logstore: str = None,
        project: str = None,
        region: str = None,
        role_arn: str = None,
    ):
        # The name of the dedicated Logstore that is used to store NAS operation logs.
        self.logstore = logstore
        # The name of the project where the dedicated Logstore resides.
        self.project = project
        # The region where the dedicated Logstore resides.
        self.region = region
        # The role that is used by NAS to access Simple Log Service.
        self.role_arn = role_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.logstore is not None:
            result['Logstore'] = self.logstore

        if self.project is not None:
            result['Project'] = self.project

        if self.region is not None:
            result['Region'] = self.region

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Logstore') is not None:
            self.logstore = m.get('Logstore')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        return self

