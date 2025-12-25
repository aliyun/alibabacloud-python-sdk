# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunWritingV2ShrinkRequest(DaraModel):
    def __init__(
        self,
        articles_shrink: str = None,
        distribute_writing: bool = None,
        gc_number_size: int = None,
        gc_number_size_tag: str = None,
        keywords_shrink: str = None,
        language: str = None,
        mini_docs_shrink: str = None,
        outline_list_shrink: str = None,
        outlines_shrink: str = None,
        prompt: str = None,
        prompt_mode: str = None,
        search_sources_shrink: str = None,
        session_id: str = None,
        source_trace_method: str = None,
        step: str = None,
        summarization_shrink: str = None,
        task_id: str = None,
        use_search: bool = None,
        workspace_id: str = None,
        writing_params_shrink: str = None,
        writing_scene: str = None,
        writing_style: str = None,
    ):
        self.articles_shrink = articles_shrink
        self.distribute_writing = distribute_writing
        self.gc_number_size = gc_number_size
        self.gc_number_size_tag = gc_number_size_tag
        self.keywords_shrink = keywords_shrink
        self.language = language
        self.mini_docs_shrink = mini_docs_shrink
        self.outline_list_shrink = outline_list_shrink
        self.outlines_shrink = outlines_shrink
        self.prompt = prompt
        self.prompt_mode = prompt_mode
        self.search_sources_shrink = search_sources_shrink
        self.session_id = session_id
        self.source_trace_method = source_trace_method
        self.step = step
        self.summarization_shrink = summarization_shrink
        self.task_id = task_id
        self.use_search = use_search
        # This parameter is required.
        self.workspace_id = workspace_id
        self.writing_params_shrink = writing_params_shrink
        self.writing_scene = writing_scene
        self.writing_style = writing_style

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.articles_shrink is not None:
            result['Articles'] = self.articles_shrink

        if self.distribute_writing is not None:
            result['DistributeWriting'] = self.distribute_writing

        if self.gc_number_size is not None:
            result['GcNumberSize'] = self.gc_number_size

        if self.gc_number_size_tag is not None:
            result['GcNumberSizeTag'] = self.gc_number_size_tag

        if self.keywords_shrink is not None:
            result['Keywords'] = self.keywords_shrink

        if self.language is not None:
            result['Language'] = self.language

        if self.mini_docs_shrink is not None:
            result['MiniDocs'] = self.mini_docs_shrink

        if self.outline_list_shrink is not None:
            result['OutlineList'] = self.outline_list_shrink

        if self.outlines_shrink is not None:
            result['Outlines'] = self.outlines_shrink

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.prompt_mode is not None:
            result['PromptMode'] = self.prompt_mode

        if self.search_sources_shrink is not None:
            result['SearchSources'] = self.search_sources_shrink

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.source_trace_method is not None:
            result['SourceTraceMethod'] = self.source_trace_method

        if self.step is not None:
            result['Step'] = self.step

        if self.summarization_shrink is not None:
            result['Summarization'] = self.summarization_shrink

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.use_search is not None:
            result['UseSearch'] = self.use_search

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        if self.writing_params_shrink is not None:
            result['WritingParams'] = self.writing_params_shrink

        if self.writing_scene is not None:
            result['WritingScene'] = self.writing_scene

        if self.writing_style is not None:
            result['WritingStyle'] = self.writing_style

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Articles') is not None:
            self.articles_shrink = m.get('Articles')

        if m.get('DistributeWriting') is not None:
            self.distribute_writing = m.get('DistributeWriting')

        if m.get('GcNumberSize') is not None:
            self.gc_number_size = m.get('GcNumberSize')

        if m.get('GcNumberSizeTag') is not None:
            self.gc_number_size_tag = m.get('GcNumberSizeTag')

        if m.get('Keywords') is not None:
            self.keywords_shrink = m.get('Keywords')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('MiniDocs') is not None:
            self.mini_docs_shrink = m.get('MiniDocs')

        if m.get('OutlineList') is not None:
            self.outline_list_shrink = m.get('OutlineList')

        if m.get('Outlines') is not None:
            self.outlines_shrink = m.get('Outlines')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('PromptMode') is not None:
            self.prompt_mode = m.get('PromptMode')

        if m.get('SearchSources') is not None:
            self.search_sources_shrink = m.get('SearchSources')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('SourceTraceMethod') is not None:
            self.source_trace_method = m.get('SourceTraceMethod')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        if m.get('Summarization') is not None:
            self.summarization_shrink = m.get('Summarization')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UseSearch') is not None:
            self.use_search = m.get('UseSearch')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        if m.get('WritingParams') is not None:
            self.writing_params_shrink = m.get('WritingParams')

        if m.get('WritingScene') is not None:
            self.writing_scene = m.get('WritingScene')

        if m.get('WritingStyle') is not None:
            self.writing_style = m.get('WritingStyle')

        return self

