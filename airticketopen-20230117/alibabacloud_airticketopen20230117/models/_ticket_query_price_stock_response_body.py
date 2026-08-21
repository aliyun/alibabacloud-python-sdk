# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_airticketopen20230117 import models as main_models
from darabonba.model import DaraModel

class TicketQueryPriceStockResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.TicketQueryPriceStockResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.TicketQueryPriceStockResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class TicketQueryPriceStockResponseBodyData(DaraModel):
    def __init__(
        self,
        calendar_price_stocks: List[main_models.TicketQueryPriceStockResponseBodyDataCalendarPriceStocks] = None,
        normal_price_stock: main_models.TicketQueryPriceStockResponseBodyDataNormalPriceStock = None,
        product_id: str = None,
        stock_type: int = None,
    ):
        self.calendar_price_stocks = calendar_price_stocks
        self.normal_price_stock = normal_price_stock
        self.product_id = product_id
        self.stock_type = stock_type

    def validate(self):
        if self.calendar_price_stocks:
            for v1 in self.calendar_price_stocks:
                 if v1:
                    v1.validate()
        if self.normal_price_stock:
            self.normal_price_stock.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CalendarPriceStocks'] = []
        if self.calendar_price_stocks is not None:
            for k1 in self.calendar_price_stocks:
                result['CalendarPriceStocks'].append(k1.to_map() if k1 else None)

        if self.normal_price_stock is not None:
            result['NormalPriceStock'] = self.normal_price_stock.to_map()

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.stock_type is not None:
            result['StockType'] = self.stock_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.calendar_price_stocks = []
        if m.get('CalendarPriceStocks') is not None:
            for k1 in m.get('CalendarPriceStocks'):
                temp_model = main_models.TicketQueryPriceStockResponseBodyDataCalendarPriceStocks()
                self.calendar_price_stocks.append(temp_model.from_map(k1))

        if m.get('NormalPriceStock') is not None:
            temp_model = main_models.TicketQueryPriceStockResponseBodyDataNormalPriceStock()
            self.normal_price_stock = temp_model.from_map(m.get('NormalPriceStock'))

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('StockType') is not None:
            self.stock_type = m.get('StockType')

        return self

class TicketQueryPriceStockResponseBodyDataNormalPriceStock(DaraModel):
    def __init__(
        self,
        distribution_price: main_models.TicketQueryPriceStockResponseBodyDataNormalPriceStockDistributionPrice = None,
        market_price: main_models.TicketQueryPriceStockResponseBodyDataNormalPriceStockMarketPrice = None,
        stock: int = None,
        suggested_price: main_models.TicketQueryPriceStockResponseBodyDataNormalPriceStockSuggestedPrice = None,
    ):
        self.distribution_price = distribution_price
        self.market_price = market_price
        self.stock = stock
        self.suggested_price = suggested_price

    def validate(self):
        if self.distribution_price:
            self.distribution_price.validate()
        if self.market_price:
            self.market_price.validate()
        if self.suggested_price:
            self.suggested_price.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.distribution_price is not None:
            result['DistributionPrice'] = self.distribution_price.to_map()

        if self.market_price is not None:
            result['MarketPrice'] = self.market_price.to_map()

        if self.stock is not None:
            result['Stock'] = self.stock

        if self.suggested_price is not None:
            result['SuggestedPrice'] = self.suggested_price.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DistributionPrice') is not None:
            temp_model = main_models.TicketQueryPriceStockResponseBodyDataNormalPriceStockDistributionPrice()
            self.distribution_price = temp_model.from_map(m.get('DistributionPrice'))

        if m.get('MarketPrice') is not None:
            temp_model = main_models.TicketQueryPriceStockResponseBodyDataNormalPriceStockMarketPrice()
            self.market_price = temp_model.from_map(m.get('MarketPrice'))

        if m.get('Stock') is not None:
            self.stock = m.get('Stock')

        if m.get('SuggestedPrice') is not None:
            temp_model = main_models.TicketQueryPriceStockResponseBodyDataNormalPriceStockSuggestedPrice()
            self.suggested_price = temp_model.from_map(m.get('SuggestedPrice'))

        return self

class TicketQueryPriceStockResponseBodyDataNormalPriceStockSuggestedPrice(DaraModel):
    def __init__(
        self,
        amount: int = None,
        currency_code: str = None,
    ):
        self.amount = amount
        self.currency_code = currency_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')

        return self

class TicketQueryPriceStockResponseBodyDataNormalPriceStockMarketPrice(DaraModel):
    def __init__(
        self,
        amount: int = None,
        currency_code: str = None,
    ):
        self.amount = amount
        self.currency_code = currency_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')

        return self

class TicketQueryPriceStockResponseBodyDataNormalPriceStockDistributionPrice(DaraModel):
    def __init__(
        self,
        amount: int = None,
        currency_code: str = None,
    ):
        self.amount = amount
        self.currency_code = currency_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')

        return self

class TicketQueryPriceStockResponseBodyDataCalendarPriceStocks(DaraModel):
    def __init__(
        self,
        date: str = None,
        distribution_price: main_models.TicketQueryPriceStockResponseBodyDataCalendarPriceStocksDistributionPrice = None,
        market_price: main_models.TicketQueryPriceStockResponseBodyDataCalendarPriceStocksMarketPrice = None,
        stock: int = None,
        suggested_price: main_models.TicketQueryPriceStockResponseBodyDataCalendarPriceStocksSuggestedPrice = None,
    ):
        self.date = date
        self.distribution_price = distribution_price
        self.market_price = market_price
        self.stock = stock
        self.suggested_price = suggested_price

    def validate(self):
        if self.distribution_price:
            self.distribution_price.validate()
        if self.market_price:
            self.market_price.validate()
        if self.suggested_price:
            self.suggested_price.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date is not None:
            result['Date'] = self.date

        if self.distribution_price is not None:
            result['DistributionPrice'] = self.distribution_price.to_map()

        if self.market_price is not None:
            result['MarketPrice'] = self.market_price.to_map()

        if self.stock is not None:
            result['Stock'] = self.stock

        if self.suggested_price is not None:
            result['SuggestedPrice'] = self.suggested_price.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')

        if m.get('DistributionPrice') is not None:
            temp_model = main_models.TicketQueryPriceStockResponseBodyDataCalendarPriceStocksDistributionPrice()
            self.distribution_price = temp_model.from_map(m.get('DistributionPrice'))

        if m.get('MarketPrice') is not None:
            temp_model = main_models.TicketQueryPriceStockResponseBodyDataCalendarPriceStocksMarketPrice()
            self.market_price = temp_model.from_map(m.get('MarketPrice'))

        if m.get('Stock') is not None:
            self.stock = m.get('Stock')

        if m.get('SuggestedPrice') is not None:
            temp_model = main_models.TicketQueryPriceStockResponseBodyDataCalendarPriceStocksSuggestedPrice()
            self.suggested_price = temp_model.from_map(m.get('SuggestedPrice'))

        return self

class TicketQueryPriceStockResponseBodyDataCalendarPriceStocksSuggestedPrice(DaraModel):
    def __init__(
        self,
        amount: int = None,
        currency_code: str = None,
    ):
        self.amount = amount
        self.currency_code = currency_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')

        return self

class TicketQueryPriceStockResponseBodyDataCalendarPriceStocksMarketPrice(DaraModel):
    def __init__(
        self,
        amount: int = None,
        currency_code: str = None,
    ):
        self.amount = amount
        self.currency_code = currency_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')

        return self

class TicketQueryPriceStockResponseBodyDataCalendarPriceStocksDistributionPrice(DaraModel):
    def __init__(
        self,
        amount: int = None,
        currency_code: str = None,
    ):
        self.amount = amount
        self.currency_code = currency_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.amount is not None:
            result['Amount'] = self.amount

        if self.currency_code is not None:
            result['CurrencyCode'] = self.currency_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('CurrencyCode') is not None:
            self.currency_code = m.get('CurrencyCode')

        return self

