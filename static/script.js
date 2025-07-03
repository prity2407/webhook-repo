async function fetchEvents() {
  const resp = await fetch('/events');
  const events = await resp.json();
  const container = document.getElementById('events');
  container.innerHTML = '';

  events.forEach(event => {
    let msg = '';
    const t = event.timestamp;
    if (event.action_type === 'push') {
      msg = `"${event.author}" pushed to "${event.to_branch}" on ${t}`;
    } else if (event.action_type === 'pull_request') {
      msg = `"${event.author}" submitted a PR from "${event.from_branch}" to "${event.to_branch}" on ${t}`;
    } else {
      msg = `"${event.author}" did ${event.action_type} on ${t}`;
    }

    const div = document.createElement('div');
    div.className = 'event';
    div.textContent = msg;
    container.appendChild(div);
  });
}

setInterval(fetchEvents, 15000);
fetchEvents();
