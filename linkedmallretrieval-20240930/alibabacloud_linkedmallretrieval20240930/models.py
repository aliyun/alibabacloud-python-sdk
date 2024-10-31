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
        html_snippet: str = None,
        html_title: str = None,
        images: List[IncludeImage] = None,
        link: str = None,
        main_text: str = None,
        mime: str = None,
        page_map: Dict[str, str] = None,
        publish_time: int = None,
        score: float = None,
        title: str = None,
    ):
        # This parameter is required.
        self.card_type = card_type
        # This parameter is required.
        self.display_link = display_link
        # This parameter is required.
        self.html_snippet = html_snippet
        # This parameter is required.
        self.html_title = html_title
        self.images = images
        # This parameter is required.
        self.link = link
        self.main_text = main_text
        self.mime = mime
        self.page_map = page_map
        # This parameter is required.
        self.publish_time = publish_time
        self.score = score
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
        if self.mime is not None:
            result['mime'] = self.mime
        if self.page_map is not None:
            result['pageMap'] = self.page_map
        if self.publish_time is not None:
            result['publishTime'] = self.publish_time
        if self.score is not None:
            result['score'] = self.score
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cardType') is not None:
            self.card_type = m.get('cardType')
        if m.get('displayLink') is not None:
            self.display_link = m.get('displayLink')
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
        if m.get('mime') is not None:
            self.mime = m.get('mime')
        if m.get('pageMap') is not None:
            self.page_map = m.get('pageMap')
        if m.get('publishTime') is not None:
            self.publish_time = m.get('publishTime')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('title') is not None:
            self.title = m.get('title')
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
        request_id: str = None,
        search_information: SearchInformation = None,
        weibo_items: List[WeiboItem] = None,
    ):
        self.page_items = page_items
        self.request_id = request_id
        self.search_information = search_information
        self.weibo_items = weibo_items

    def validate(self):
        if self.page_items:
            for k in self.page_items:
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
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
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('searchInformation') is not None:
            temp_model = SearchInformation()
            self.search_information = temp_model.from_map(m['searchInformation'])
        self.weibo_items = []
        if m.get('weiboItems') is not None:
            for k in m.get('weiboItems'):
                temp_model = WeiboItem()
                self.weibo_items.append(temp_model.from_map(k))
        return self


class GenericSearchRequest(TeaModel):
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


