# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from farquest import Farquest, AsyncFarquest

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_count(self, client: Farquest) -> None:
        completion = client.quest.completions.count(
            "string",
        )
        assert completion is None

    @parametrize
    def test_raw_response_count(self, client: Farquest) -> None:
        response = client.quest.completions.with_raw_response.count(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert completion is None

    @parametrize
    def test_streaming_response_count(self, client: Farquest) -> None:
        with client.quest.completions.with_streaming_response.count(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert completion is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_count(self, client: Farquest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.quest.completions.with_raw_response.count(
                "",
            )


class TestAsyncCompletions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_count(self, async_client: AsyncFarquest) -> None:
        completion = await async_client.quest.completions.count(
            "string",
        )
        assert completion is None

    @parametrize
    async def test_raw_response_count(self, async_client: AsyncFarquest) -> None:
        response = await async_client.quest.completions.with_raw_response.count(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert completion is None

    @parametrize
    async def test_streaming_response_count(self, async_client: AsyncFarquest) -> None:
        async with async_client.quest.completions.with_streaming_response.count(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert completion is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_count(self, async_client: AsyncFarquest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.quest.completions.with_raw_response.count(
                "",
            )
