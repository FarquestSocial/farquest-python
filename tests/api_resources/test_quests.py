# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from farquest import Farquest, AsyncFarquest

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuests:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_complete(self, client: Farquest) -> None:
        quest = client.quests.complete(
            correlation_id="string",
            quest_id="string",
        )
        assert quest is None

    @parametrize
    def test_raw_response_complete(self, client: Farquest) -> None:
        response = client.quests.with_raw_response.complete(
            correlation_id="string",
            quest_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quest = response.parse()
        assert quest is None

    @parametrize
    def test_streaming_response_complete(self, client: Farquest) -> None:
        with client.quests.with_streaming_response.complete(
            correlation_id="string",
            quest_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quest = response.parse()
            assert quest is None

        assert cast(Any, response.is_closed) is True


class TestAsyncQuests:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_complete(self, async_client: AsyncFarquest) -> None:
        quest = await async_client.quests.complete(
            correlation_id="string",
            quest_id="string",
        )
        assert quest is None

    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncFarquest) -> None:
        response = await async_client.quests.with_raw_response.complete(
            correlation_id="string",
            quest_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quest = await response.parse()
        assert quest is None

    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncFarquest) -> None:
        async with async_client.quests.with_streaming_response.complete(
            correlation_id="string",
            quest_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quest = await response.parse()
            assert quest is None

        assert cast(Any, response.is_closed) is True
