# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AISearchQuery(TeaModel):
    def __init__(
        self,
        card: str = None,
        card_query: str = None,
        page: int = None,
        query: str = None,
        search_engine: str = None,
        search_plan: str = None,
        session_id: str = None,
        time_range: str = None,
    ):
        self.card = card
        self.card_query = card_query
        self.page = page
        self.query = query
        self.search_engine = search_engine
        self.search_plan = search_plan
        self.session_id = session_id
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card is not None:
            result['card'] = self.card
        if self.card_query is not None:
            result['cardQuery'] = self.card_query
        if self.page is not None:
            result['page'] = self.page
        if self.query is not None:
            result['query'] = self.query
        if self.search_engine is not None:
            result['searchEngine'] = self.search_engine
        if self.search_plan is not None:
            result['searchPlan'] = self.search_plan
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.time_range is not None:
            result['timeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('card') is not None:
            self.card = m.get('card')
        if m.get('cardQuery') is not None:
            self.card_query = m.get('cardQuery')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('searchEngine') is not None:
            self.search_engine = m.get('searchEngine')
        if m.get('searchPlan') is not None:
            self.search_plan = m.get('searchPlan')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')
        return self


class IncludeImage(TeaModel):
    def __init__(
        self,
        height: int = None,
        image_link: str = None,
        width: int = None,
    ):
        self.height = height
        self.image_link = image_link
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['height'] = self.height
        if self.image_link is not None:
            result['imageLink'] = self.image_link
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('imageLink') is not None:
            self.image_link = m.get('imageLink')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class ScorePageItem(TeaModel):
    def __init__(
        self,
        card_type: str = None,
        display_link: str = None,
        host_logo: str = None,
        hostname: str = None,
        html_snippet: str = None,
        html_title: str = None,
        images: List[IncludeImage] = None,
        link: str = None,
        main_text: str = None,
        markdown_text: str = None,
        mime: str = None,
        page_map: Dict[str, str] = None,
        publish_time: int = None,
        score: float = None,
        site_label: str = None,
        snippet: str = None,
        summary: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.card_type = card_type
        # This parameter is required.
        self.display_link = display_link
        self.host_logo = host_logo
        self.hostname = hostname
        # This parameter is required.
        self.html_snippet = html_snippet
        # This parameter is required.
        self.html_title = html_title
        self.images = images
        # This parameter is required.
        self.link = link
        self.main_text = main_text
        self.markdown_text = markdown_text
        self.mime = mime
        self.page_map = page_map
        # This parameter is required.
        self.publish_time = publish_time
        self.score = score
        self.site_label = site_label
        self.snippet = snippet
        self.summary = summary
        # This parameter is required.
        self.title = title

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_type is not None:
            result['cardType'] = self.card_type
        if self.display_link is not None:
            result['displayLink'] = self.display_link
        if self.host_logo is not None:
            result['hostLogo'] = self.host_logo
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.html_snippet is not None:
            result['htmlSnippet'] = self.html_snippet
        if self.html_title is not None:
            result['htmlTitle'] = self.html_title
        result['images'] = []
        if self.images is not None:
            for k in self.images:
                result['images'].append(k.to_map() if k else None)
        if self.link is not None:
            result['link'] = self.link
        if self.main_text is not None:
            result['mainText'] = self.main_text
        if self.markdown_text is not None:
            result['markdownText'] = self.markdown_text
        if self.mime is not None:
            result['mime'] = self.mime
        if self.page_map is not None:
            result['pageMap'] = self.page_map
        if self.publish_time is not None:
            result['publishTime'] = self.publish_time
        if self.score is not None:
            result['score'] = self.score
        if self.site_label is not None:
            result['siteLabel'] = self.site_label
        if self.snippet is not None:
            result['snippet'] = self.snippet
        if self.summary is not None:
            result['summary'] = self.summary
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cardType') is not None:
            self.card_type = m.get('cardType')
        if m.get('displayLink') is not None:
            self.display_link = m.get('displayLink')
        if m.get('hostLogo') is not None:
            self.host_logo = m.get('hostLogo')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('htmlSnippet') is not None:
            self.html_snippet = m.get('htmlSnippet')
        if m.get('htmlTitle') is not None:
            self.html_title = m.get('htmlTitle')
        self.images = []
        if m.get('images') is not None:
            for k in m.get('images'):
                temp_model = IncludeImage()
                self.images.append(temp_model.from_map(k))
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('mainText') is not None:
            self.main_text = m.get('mainText')
        if m.get('markdownText') is not None:
            self.markdown_text = m.get('markdownText')
        if m.get('mime') is not None:
            self.mime = m.get('mime')
        if m.get('pageMap') is not None:
            self.page_map = m.get('pageMap')
        if m.get('publishTime') is not None:
            self.publish_time = m.get('publishTime')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('siteLabel') is not None:
            self.site_label = m.get('siteLabel')
        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class QueryContextOriginalQuery(TeaModel):
    def __init__(
        self,
        industry: str = None,
        page: str = None,
        query: str = None,
        time_range: str = None,
    ):
        self.industry = industry
        self.page = page
        self.query = query
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.industry is not None:
            result['industry'] = self.industry
        if self.page is not None:
            result['page'] = self.page
        if self.query is not None:
            result['query'] = self.query
        if self.time_range is not None:
            result['timeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')
        return self


class QueryContextRewrite(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        time_range: str = None,
    ):
        self.enabled = enabled
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.time_range is not None:
            result['timeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')
        return self


class QueryContext(TeaModel):
    def __init__(
        self,
        original_query: QueryContextOriginalQuery = None,
        rewrite: QueryContextRewrite = None,
    ):
        self.original_query = original_query
        self.rewrite = rewrite

    def validate(self):
        if self.original_query:
            self.original_query.validate()
        if self.rewrite:
            self.rewrite.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_query is not None:
            result['originalQuery'] = self.original_query.to_map()
        if self.rewrite is not None:
            result['rewrite'] = self.rewrite.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originalQuery') is not None:
            temp_model = QueryContextOriginalQuery()
            self.original_query = temp_model.from_map(m['originalQuery'])
        if m.get('rewrite') is not None:
            temp_model = QueryContextRewrite()
            self.rewrite = temp_model.from_map(m['rewrite'])
        return self


class SceneItem(TeaModel):
    def __init__(
        self,
        detail: str = None,
        type: str = None,
    ):
        self.detail = detail
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['detail'] = self.detail
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class SearchInformation(TeaModel):
    def __init__(
        self,
        search_time: int = None,
        total: int = None,
    ):
        self.search_time = search_time
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search_time is not None:
            result['searchTime'] = self.search_time
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('searchTime') is not None:
            self.search_time = m.get('searchTime')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class WeiboItem(TeaModel):
    def __init__(
        self,
        card_type: str = None,
        homepage_link: str = None,
        html_snippet: str = None,
        images: List[str] = None,
        link: str = None,
        publish_display_time: str = None,
        username: str = None,
    ):
        # This parameter is required.
        self.card_type = card_type
        self.homepage_link = homepage_link
        # This parameter is required.
        self.html_snippet = html_snippet
        self.images = images
        # This parameter is required.
        self.link = link
        # This parameter is required.
        self.publish_display_time = publish_display_time
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.card_type is not None:
            result['cardType'] = self.card_type
        if self.homepage_link is not None:
            result['homepageLink'] = self.homepage_link
        if self.html_snippet is not None:
            result['htmlSnippet'] = self.html_snippet
        if self.images is not None:
            result['images'] = self.images
        if self.link is not None:
            result['link'] = self.link
        if self.publish_display_time is not None:
            result['publishDisplayTime'] = self.publish_display_time
        if self.username is not None:
            result['username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cardType') is not None:
            self.card_type = m.get('cardType')
        if m.get('homepageLink') is not None:
            self.homepage_link = m.get('homepageLink')
        if m.get('htmlSnippet') is not None:
            self.html_snippet = m.get('htmlSnippet')
        if m.get('images') is not None:
            self.images = m.get('images')
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('publishDisplayTime') is not None:
            self.publish_display_time = m.get('publishDisplayTime')
        if m.get('username') is not None:
            self.username = m.get('username')
        return self


class GenericSearchResult(TeaModel):
    def __init__(
        self,
        page_items: List[ScorePageItem] = None,
        query_context: QueryContext = None,
        request_id: str = None,
        scene_items: List[SceneItem] = None,
        search_information: SearchInformation = None,
        weibo_items: List[WeiboItem] = None,
    ):
        self.page_items = page_items
        self.query_context = query_context
        self.request_id = request_id
        self.scene_items = scene_items
        self.search_information = search_information
        self.weibo_items = weibo_items

    def validate(self):
        if self.page_items:
            for k in self.page_items:
                if k:
                    k.validate()
        if self.query_context:
            self.query_context.validate()
        if self.scene_items:
            for k in self.scene_items:
                if k:
                    k.validate()
        if self.search_information:
            self.search_information.validate()
        if self.weibo_items:
            for k in self.weibo_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['pageItems'] = []
        if self.page_items is not None:
            for k in self.page_items:
                result['pageItems'].append(k.to_map() if k else None)
        if self.query_context is not None:
            result['queryContext'] = self.query_context.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['sceneItems'] = []
        if self.scene_items is not None:
            for k in self.scene_items:
                result['sceneItems'].append(k.to_map() if k else None)
        if self.search_information is not None:
            result['searchInformation'] = self.search_information.to_map()
        result['weiboItems'] = []
        if self.weibo_items is not None:
            for k in self.weibo_items:
                result['weiboItems'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_items = []
        if m.get('pageItems') is not None:
            for k in m.get('pageItems'):
                temp_model = ScorePageItem()
                self.page_items.append(temp_model.from_map(k))
        if m.get('queryContext') is not None:
            temp_model = QueryContext()
            self.query_context = temp_model.from_map(m['queryContext'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.scene_items = []
        if m.get('sceneItems') is not None:
            for k in m.get('sceneItems'):
                temp_model = SceneItem()
                self.scene_items.append(temp_model.from_map(k))
        if m.get('searchInformation') is not None:
            temp_model = SearchInformation()
            self.search_information = temp_model.from_map(m['searchInformation'])
        self.weibo_items = []
        if m.get('weiboItems') is not None:
            for k in m.get('weiboItems'):
                temp_model = WeiboItem()
                self.weibo_items.append(temp_model.from_map(k))
        return self


class GlobalPageItem(TeaModel):
    def __init__(
        self,
        link: str = None,
        snippet: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.link = link
        self.snippet = snippet
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.link is not None:
            result['link'] = self.link
        if self.snippet is not None:
            result['snippet'] = self.snippet
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class GlobalQueryContextOriginalQuery(TeaModel):
    def __init__(
        self,
        page: str = None,
        query: str = None,
        time_range: str = None,
    ):
        self.page = page
        self.query = query
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.query is not None:
            result['query'] = self.query
        if self.time_range is not None:
            result['timeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')
        return self


class GlobalQueryContext(TeaModel):
    def __init__(
        self,
        original_query: GlobalQueryContextOriginalQuery = None,
    ):
        self.original_query = original_query

    def validate(self):
        if self.original_query:
            self.original_query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_query is not None:
            result['originalQuery'] = self.original_query.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originalQuery') is not None:
            temp_model = GlobalQueryContextOriginalQuery()
            self.original_query = temp_model.from_map(m['originalQuery'])
        return self


class GlobalSceneItem(TeaModel):
    def __init__(
        self,
        detail: str = None,
        type: str = None,
    ):
        self.detail = detail
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['detail'] = self.detail
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GlobalSearchInformation(TeaModel):
    def __init__(
        self,
        search_time: int = None,
        total: int = None,
    ):
        self.search_time = search_time
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search_time is not None:
            result['searchTime'] = self.search_time
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('searchTime') is not None:
            self.search_time = m.get('searchTime')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GlobalSearchResult(TeaModel):
    def __init__(
        self,
        page_items: List[GlobalPageItem] = None,
        query_context: GlobalQueryContext = None,
        request_id: str = None,
        scene_items: List[GlobalSceneItem] = None,
        search_information: GlobalSearchInformation = None,
    ):
        self.page_items = page_items
        self.query_context = query_context
        self.request_id = request_id
        self.scene_items = scene_items
        self.search_information = search_information

    def validate(self):
        if self.page_items:
            for k in self.page_items:
                if k:
                    k.validate()
        if self.query_context:
            self.query_context.validate()
        if self.scene_items:
            for k in self.scene_items:
                if k:
                    k.validate()
        if self.search_information:
            self.search_information.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['pageItems'] = []
        if self.page_items is not None:
            for k in self.page_items:
                result['pageItems'].append(k.to_map() if k else None)
        if self.query_context is not None:
            result['queryContext'] = self.query_context.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['sceneItems'] = []
        if self.scene_items is not None:
            for k in self.scene_items:
                result['sceneItems'].append(k.to_map() if k else None)
        if self.search_information is not None:
            result['searchInformation'] = self.search_information.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.page_items = []
        if m.get('pageItems') is not None:
            for k in m.get('pageItems'):
                temp_model = GlobalPageItem()
                self.page_items.append(temp_model.from_map(k))
        if m.get('queryContext') is not None:
            temp_model = GlobalQueryContext()
            self.query_context = temp_model.from_map(m['queryContext'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.scene_items = []
        if m.get('sceneItems') is not None:
            for k in m.get('sceneItems'):
                temp_model = GlobalSceneItem()
                self.scene_items.append(temp_model.from_map(k))
        if m.get('searchInformation') is not None:
            temp_model = GlobalSearchInformation()
            self.search_information = temp_model.from_map(m['searchInformation'])
        return self


class RequestContents(TeaModel):
    def __init__(
        self,
        main_text: bool = None,
        markdown_text: bool = None,
        rerank_score: bool = None,
        summary: bool = None,
    ):
        self.main_text = main_text
        self.markdown_text = markdown_text
        self.rerank_score = rerank_score
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.main_text is not None:
            result['mainText'] = self.main_text
        if self.markdown_text is not None:
            result['markdownText'] = self.markdown_text
        if self.rerank_score is not None:
            result['rerankScore'] = self.rerank_score
        if self.summary is not None:
            result['summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mainText') is not None:
            self.main_text = m.get('mainText')
        if m.get('markdownText') is not None:
            self.markdown_text = m.get('markdownText')
        if m.get('rerankScore') is not None:
            self.rerank_score = m.get('rerankScore')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        return self


class SearchCredits(TeaModel):
    def __init__(
        self,
        generic_text_search: int = None,
    ):
        self.generic_text_search = generic_text_search

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.generic_text_search is not None:
            result['genericTextSearch'] = self.generic_text_search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('genericTextSearch') is not None:
            self.generic_text_search = m.get('genericTextSearch')
        return self


class ValueAddedCredits(TeaModel):
    def __init__(
        self,
        advanced: int = None,
        summary: int = None,
    ):
        self.advanced = advanced
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.advanced is not None:
            result['advanced'] = self.advanced
        if self.summary is not None:
            result['summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('advanced') is not None:
            self.advanced = m.get('advanced')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        return self


class UnifiedCostCredits(TeaModel):
    def __init__(
        self,
        search: SearchCredits = None,
        value_added: ValueAddedCredits = None,
    ):
        self.search = search
        self.value_added = value_added

    def validate(self):
        if self.search:
            self.search.validate()
        if self.value_added:
            self.value_added.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search is not None:
            result['search'] = self.search.to_map()
        if self.value_added is not None:
            result['valueAdded'] = self.value_added.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('search') is not None:
            temp_model = SearchCredits()
            self.search = temp_model.from_map(m['search'])
        if m.get('valueAdded') is not None:
            temp_model = ValueAddedCredits()
            self.value_added = temp_model.from_map(m['valueAdded'])
        return self


class UnifiedOriginalQuery(TeaModel):
    def __init__(
        self,
        query: str = None,
        time_range: str = None,
    ):
        self.query = query
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query is not None:
            result['query'] = self.query
        if self.time_range is not None:
            result['timeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')
        return self


class UnifiedPageItem(TeaModel):
    def __init__(
        self,
        host_logo: str = None,
        hostname: str = None,
        images: List[str] = None,
        link: str = None,
        main_text: str = None,
        markdown_text: str = None,
        published_time: str = None,
        rerank_score: float = None,
        snippet: str = None,
        summary: str = None,
        title: str = None,
    ):
        self.host_logo = host_logo
        self.hostname = hostname
        self.images = images
        self.link = link
        self.main_text = main_text
        self.markdown_text = markdown_text
        self.published_time = published_time
        self.rerank_score = rerank_score
        self.snippet = snippet
        self.summary = summary
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_logo is not None:
            result['hostLogo'] = self.host_logo
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.images is not None:
            result['images'] = self.images
        if self.link is not None:
            result['link'] = self.link
        if self.main_text is not None:
            result['mainText'] = self.main_text
        if self.markdown_text is not None:
            result['markdownText'] = self.markdown_text
        if self.published_time is not None:
            result['publishedTime'] = self.published_time
        if self.rerank_score is not None:
            result['rerankScore'] = self.rerank_score
        if self.snippet is not None:
            result['snippet'] = self.snippet
        if self.summary is not None:
            result['summary'] = self.summary
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostLogo') is not None:
            self.host_logo = m.get('hostLogo')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('images') is not None:
            self.images = m.get('images')
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('mainText') is not None:
            self.main_text = m.get('mainText')
        if m.get('markdownText') is not None:
            self.markdown_text = m.get('markdownText')
        if m.get('publishedTime') is not None:
            self.published_time = m.get('publishedTime')
        if m.get('rerankScore') is not None:
            self.rerank_score = m.get('rerankScore')
        if m.get('snippet') is not None:
            self.snippet = m.get('snippet')
        if m.get('summary') is not None:
            self.summary = m.get('summary')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class UnifiedRewrite(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        time_range: str = None,
    ):
        self.enabled = enabled
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.time_range is not None:
            result['timeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')
        return self


class UnifiedQueryContext(TeaModel):
    def __init__(
        self,
        engine_type: str = None,
        original_query: UnifiedOriginalQuery = None,
        rewrite: UnifiedRewrite = None,
    ):
        self.engine_type = engine_type
        self.original_query = original_query
        self.rewrite = rewrite

    def validate(self):
        if self.original_query:
            self.original_query.validate()
        if self.rewrite:
            self.rewrite.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.engine_type is not None:
            result['engineType'] = self.engine_type
        if self.original_query is not None:
            result['originalQuery'] = self.original_query.to_map()
        if self.rewrite is not None:
            result['rewrite'] = self.rewrite.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('originalQuery') is not None:
            temp_model = UnifiedOriginalQuery()
            self.original_query = temp_model.from_map(m['originalQuery'])
        if m.get('rewrite') is not None:
            temp_model = UnifiedRewrite()
            self.rewrite = temp_model.from_map(m['rewrite'])
        return self


class UnifiedSceneItem(TeaModel):
    def __init__(
        self,
        detail: str = None,
        type: str = None,
    ):
        self.detail = detail
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['detail'] = self.detail
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('detail') is not None:
            self.detail = m.get('detail')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UnifiedSearchInformation(TeaModel):
    def __init__(
        self,
        search_time: int = None,
    ):
        self.search_time = search_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search_time is not None:
            result['searchTime'] = self.search_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('searchTime') is not None:
            self.search_time = m.get('searchTime')
        return self


class UnifiedSearchInput(TeaModel):
    def __init__(
        self,
        category: str = None,
        contents: RequestContents = None,
        engine_type: str = None,
        location: str = None,
        query: str = None,
        time_range: str = None,
    ):
        self.category = category
        self.contents = contents
        self.engine_type = engine_type
        self.location = location
        self.query = query
        self.time_range = time_range

    def validate(self):
        if self.contents:
            self.contents.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.contents is not None:
            result['contents'] = self.contents.to_map()
        if self.engine_type is not None:
            result['engineType'] = self.engine_type
        if self.location is not None:
            result['location'] = self.location
        if self.query is not None:
            result['query'] = self.query
        if self.time_range is not None:
            result['timeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('contents') is not None:
            temp_model = RequestContents()
            self.contents = temp_model.from_map(m['contents'])
        if m.get('engineType') is not None:
            self.engine_type = m.get('engineType')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')
        return self


class UnifiedSearchOutput(TeaModel):
    def __init__(
        self,
        cost_credits: UnifiedCostCredits = None,
        page_items: List[UnifiedPageItem] = None,
        query_context: UnifiedQueryContext = None,
        request_id: str = None,
        scene_items: List[UnifiedSceneItem] = None,
        search_information: UnifiedSearchInformation = None,
    ):
        self.cost_credits = cost_credits
        self.page_items = page_items
        self.query_context = query_context
        self.request_id = request_id
        self.scene_items = scene_items
        self.search_information = search_information

    def validate(self):
        if self.cost_credits:
            self.cost_credits.validate()
        if self.page_items:
            for k in self.page_items:
                if k:
                    k.validate()
        if self.query_context:
            self.query_context.validate()
        if self.scene_items:
            for k in self.scene_items:
                if k:
                    k.validate()
        if self.search_information:
            self.search_information.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cost_credits is not None:
            result['costCredits'] = self.cost_credits.to_map()
        result['pageItems'] = []
        if self.page_items is not None:
            for k in self.page_items:
                result['pageItems'].append(k.to_map() if k else None)
        if self.query_context is not None:
            result['queryContext'] = self.query_context.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['sceneItems'] = []
        if self.scene_items is not None:
            for k in self.scene_items:
                result['sceneItems'].append(k.to_map() if k else None)
        if self.search_information is not None:
            result['searchInformation'] = self.search_information.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('costCredits') is not None:
            temp_model = UnifiedCostCredits()
            self.cost_credits = temp_model.from_map(m['costCredits'])
        self.page_items = []
        if m.get('pageItems') is not None:
            for k in m.get('pageItems'):
                temp_model = UnifiedPageItem()
                self.page_items.append(temp_model.from_map(k))
        if m.get('queryContext') is not None:
            temp_model = UnifiedQueryContext()
            self.query_context = temp_model.from_map(m['queryContext'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.scene_items = []
        if m.get('sceneItems') is not None:
            for k in m.get('sceneItems'):
                temp_model = UnifiedSceneItem()
                self.scene_items.append(temp_model.from_map(k))
        if m.get('searchInformation') is not None:
            temp_model = UnifiedSearchInformation()
            self.search_information = temp_model.from_map(m['searchInformation'])
        return self


class AiSearchRequest(TeaModel):
    def __init__(
        self,
        industry: str = None,
        page: int = None,
        query: str = None,
        session_id: str = None,
        time_range: str = None,
    ):
        self.industry = industry
        self.page = page
        # This parameter is required.
        self.query = query
        self.session_id = session_id
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.industry is not None:
            result['industry'] = self.industry
        if self.page is not None:
            result['page'] = self.page
        if self.query is not None:
            result['query'] = self.query
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.time_range is not None:
            result['timeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')
        return self


class AiSearchResponseBodyHeaderQueryContextOriginalQuery(TeaModel):
    def __init__(
        self,
        industry: str = None,
        page: int = None,
        query: str = None,
        time_range: str = None,
    ):
        self.industry = industry
        self.page = page
        self.query = query
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.industry is not None:
            result['industry'] = self.industry
        if self.page is not None:
            result['page'] = self.page
        if self.query is not None:
            result['query'] = self.query
        if self.time_range is not None:
            result['timeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')
        return self


class AiSearchResponseBodyHeaderQueryContextRewrite(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        time_range: str = None,
    ):
        self.enabled = enabled
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.time_range is not None:
            result['timeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')
        return self


class AiSearchResponseBodyHeaderQueryContext(TeaModel):
    def __init__(
        self,
        original_query: AiSearchResponseBodyHeaderQueryContextOriginalQuery = None,
        rewrite: AiSearchResponseBodyHeaderQueryContextRewrite = None,
    ):
        self.original_query = original_query
        self.rewrite = rewrite

    def validate(self):
        if self.original_query:
            self.original_query.validate()
        if self.rewrite:
            self.rewrite.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.original_query is not None:
            result['originalQuery'] = self.original_query.to_map()
        if self.rewrite is not None:
            result['rewrite'] = self.rewrite.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('originalQuery') is not None:
            temp_model = AiSearchResponseBodyHeaderQueryContextOriginalQuery()
            self.original_query = temp_model.from_map(m['originalQuery'])
        if m.get('rewrite') is not None:
            temp_model = AiSearchResponseBodyHeaderQueryContextRewrite()
            self.rewrite = temp_model.from_map(m['rewrite'])
        return self


class AiSearchResponseBodyHeader(TeaModel):
    def __init__(
        self,
        event: str = None,
        event_id: str = None,
        query_context: AiSearchResponseBodyHeaderQueryContext = None,
        response_time: int = None,
    ):
        self.event = event
        self.event_id = event_id
        self.query_context = query_context
        self.response_time = response_time

    def validate(self):
        if self.query_context:
            self.query_context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event is not None:
            result['event'] = self.event
        if self.event_id is not None:
            result['eventId'] = self.event_id
        if self.query_context is not None:
            result['queryContext'] = self.query_context.to_map()
        if self.response_time is not None:
            result['responseTime'] = self.response_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('event') is not None:
            self.event = m.get('event')
        if m.get('eventId') is not None:
            self.event_id = m.get('eventId')
        if m.get('queryContext') is not None:
            temp_model = AiSearchResponseBodyHeaderQueryContext()
            self.query_context = temp_model.from_map(m['queryContext'])
        if m.get('responseTime') is not None:
            self.response_time = m.get('responseTime')
        return self


class AiSearchResponseBody(TeaModel):
    def __init__(
        self,
        header: AiSearchResponseBodyHeader = None,
        payload: str = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header is not None:
            result['header'] = self.header.to_map()
        if self.payload is not None:
            result['payload'] = self.payload
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('header') is not None:
            temp_model = AiSearchResponseBodyHeader()
            self.header = temp_model.from_map(m['header'])
        if m.get('payload') is not None:
            self.payload = m.get('payload')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class AiSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AiSearchResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AiSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenericAdvancedSearchRequest(TeaModel):
    def __init__(
        self,
        industry: str = None,
        query: str = None,
        session_id: str = None,
        time_range: str = None,
    ):
        self.industry = industry
        # This parameter is required.
        self.query = query
        self.session_id = session_id
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.industry is not None:
            result['industry'] = self.industry
        if self.query is not None:
            result['query'] = self.query
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.time_range is not None:
            result['timeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')
        return self


class GenericAdvancedSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenericSearchResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenericSearchResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GenericSearchRequest(TeaModel):
    def __init__(
        self,
        enable_rerank: bool = None,
        industry: str = None,
        page: int = None,
        query: str = None,
        return_main_text: bool = None,
        return_markdown_text: bool = None,
        return_summary: bool = None,
        session_id: str = None,
        time_range: str = None,
    ):
        self.enable_rerank = enable_rerank
        self.industry = industry
        self.page = page
        # This parameter is required.
        self.query = query
        self.return_main_text = return_main_text
        self.return_markdown_text = return_markdown_text
        self.return_summary = return_summary
        self.session_id = session_id
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_rerank is not None:
            result['enableRerank'] = self.enable_rerank
        if self.industry is not None:
            result['industry'] = self.industry
        if self.page is not None:
            result['page'] = self.page
        if self.query is not None:
            result['query'] = self.query
        if self.return_main_text is not None:
            result['returnMainText'] = self.return_main_text
        if self.return_markdown_text is not None:
            result['returnMarkdownText'] = self.return_markdown_text
        if self.return_summary is not None:
            result['returnSummary'] = self.return_summary
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        if self.time_range is not None:
            result['timeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableRerank') is not None:
            self.enable_rerank = m.get('enableRerank')
        if m.get('industry') is not None:
            self.industry = m.get('industry')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('returnMainText') is not None:
            self.return_main_text = m.get('returnMainText')
        if m.get('returnMarkdownText') is not None:
            self.return_markdown_text = m.get('returnMarkdownText')
        if m.get('returnSummary') is not None:
            self.return_summary = m.get('returnSummary')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')
        return self


class GenericSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenericSearchResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GenericSearchResult()
            self.body = temp_model.from_map(m['body'])
        return self


class GlobalSearchRequest(TeaModel):
    def __init__(
        self,
        page: int = None,
        page_size: int = None,
        query: str = None,
        time_range: str = None,
    ):
        self.page = page
        self.page_size = page_size
        # This parameter is required.
        self.query = query
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page is not None:
            result['page'] = self.page
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.query is not None:
            result['query'] = self.query
        if self.time_range is not None:
            result['timeRange'] = self.time_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')
        return self


class GlobalSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GlobalSearchResult = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GlobalSearchResult()
            self.body = temp_model.from_map(m['body'])
        return self


class UnifiedSearchRequest(TeaModel):
    def __init__(
        self,
        body: UnifiedSearchInput = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = UnifiedSearchInput()
            self.body = temp_model.from_map(m['body'])
        return self


class UnifiedSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnifiedSearchOutput = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UnifiedSearchOutput()
            self.body = temp_model.from_map(m['body'])
        return self


