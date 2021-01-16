new Vue ({
	el: '#taskList',
	data: {
		title: 'to do list',
		tasks: [
			{ name: 'Start a new pen' },
			{ name: 'Read a book' },
			{ name: 'Meeting with team' }
		]
	},
	methods: {
		newItem: function() {
			if (!this.tasks.name) {
				return
			}
			this.tasks.push ( {
				name: this.tasks.name,
				del: ''
			});
      this.tasks.name = "";
		},
	}
})
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
				<td>${url}</td>
				<td>${url_info}</td>
				<td>${url_meta_image}</td>
				<td>${url_meta_title}</td>
				<td>${url_meta_description}</td>
			</tr>
		</table>
	</label>
			<span onclick="delete_url()" class="delete-btn" title="Delete Task"></span>
</li>

	`
	$('#').append(temp_html)
}

function url_insert() {
	let url_give = $('#url_s').val();
	let url_info_give = $('#url').val();
	$.ajax({

	})
}