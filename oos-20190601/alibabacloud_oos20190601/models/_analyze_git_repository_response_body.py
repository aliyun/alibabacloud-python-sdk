# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_oos20190601 import models as main_models
from darabonba.model import DaraModel

class AnalyzeGitRepositoryResponseBody(DaraModel):
    def __init__(
        self,
        analysis_results: List[main_models.AnalyzeGitRepositoryResponseBodyAnalysisResults] = None,
        count: int = None,
        request_id: str = None,
    ):
        self.analysis_results = analysis_results
        self.count = count
        self.request_id = request_id

    def validate(self):
        if self.analysis_results:
            for v1 in self.analysis_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AnalysisResults'] = []
        if self.analysis_results is not None:
            for k1 in self.analysis_results:
                result['AnalysisResults'].append(k1.to_map() if k1 else None)

        if self.count is not None:
            result['Count'] = self.count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.analysis_results = []
        if m.get('AnalysisResults') is not None:
            for k1 in m.get('AnalysisResults'):
                temp_model = main_models.AnalyzeGitRepositoryResponseBodyAnalysisResults()
                self.analysis_results.append(temp_model.from_map(k1))

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class AnalyzeGitRepositoryResponseBodyAnalysisResults(DaraModel):
    def __init__(
        self,
        build_files: List[main_models.AnalyzeGitRepositoryResponseBodyAnalysisResultsBuildFiles] = None,
        build_type: str = None,
        runtime_type: str = None,
    ):
        self.build_files = build_files
        self.build_type = build_type
        self.runtime_type = runtime_type

    def validate(self):
        if self.build_files:
            for v1 in self.build_files:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BuildFiles'] = []
        if self.build_files is not None:
            for k1 in self.build_files:
                result['BuildFiles'].append(k1.to_map() if k1 else None)

        if self.build_type is not None:
            result['BuildType'] = self.build_type

        if self.runtime_type is not None:
            result['RuntimeType'] = self.runtime_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.build_files = []
        if m.get('BuildFiles') is not None:
            for k1 in m.get('BuildFiles'):
                temp_model = main_models.AnalyzeGitRepositoryResponseBodyAnalysisResultsBuildFiles()
                self.build_files.append(temp_model.from_map(k1))

        if m.get('BuildType') is not None:
            self.build_type = m.get('BuildType')

        if m.get('RuntimeType') is not None:
            self.runtime_type = m.get('RuntimeType')

        return self



class AnalyzeGitRepositoryResponseBodyAnalysisResultsBuildFiles(DaraModel):
    def __init__(
        self,
        file_type: str = None,
        paths: List[str] = None,
    ):
        self.file_type = file_type
        self.paths = paths

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.paths is not None:
            result['Paths'] = self.paths

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        return self

