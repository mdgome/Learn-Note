function url_get() {
	$.ajax({
		type: "GET",
		url: "/url/get",
		data: {},
		success: function (response) {
			let url_list = response['url_list']
			for(let i = 0; i< url_list.length; i++) {
				append_url(
					url_list[i]['url'],
					url_list[i]['url_info'],
					url_list[i]['url_meta_image'],
					url_list[i]['url_meta_title'],
					url_list[i]['url_meta_description']
				)
			}
		}
	})
}
function append_url(url, url_info, url_meta_image, url_meta_title, url_meta_description) {
	temp_html = `
	<li class="task-list-item" >
	<label id="url-table" class="task-list-item-label">
		<table>
			<tr>
				<td class="url_name_hide">${url}</td>
				<td class="url_name_hide">${url_info}</td>
				<td>${url_meta_image}</td>
				<td class="url_name_hide">${url_meta_title}</td>
				<td class="url_name_hide">${url_meta_description}</td>
			</tr>
		</table>
	</label>
			<span onclick="delete_url()" class="delete-btn" title="Delete Task"></span>
</li>

	`
	$('#url_list').append(temp_html)
}

function url_insert() {
	let url_give = $('#url_site').val();
	let url_info_give = $('#url_info').val();
	$.ajax({
		type: "POST",
		url: "/url/insert",
		data: {
			'url_give': url_give,
			'url_info_give': url_info_give
		},
		success: function (response) {
			if(response["result" == "success"]) {
				window.location.reload();
			}
		}
	})
}